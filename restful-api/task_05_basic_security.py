#!/usr/bin/python3
from flask import Flask, jsonify, request
from flask_httpauth import HTTPBasicAuth
from flask_jwt_extended import JWTManager, jwt_required, create_access_token, get_jwt_identity, get_jwt_claims
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
app.config['JWT_SECRET_KEY'] = 'super-secret'  # Change this to a secure secret key in production
jwt = JWTManager(app)
auth = HTTPBasicAuth()

# Dictionary to store user data
users = {
    "user1": {"username": "user1", "password": generate_password_hash("password"), "role": "user"},
    "admin1": {"username": "admin1", "password": generate_password_hash("password"), "role": "admin"}
}

# Basic Authentication

@auth.verify_password
def verify_password(username, password):
    if username in users and check_password_hash(users[username]['password'], password):
        return username

@app.route('/basic-protected')
@auth.login_required
def basic_protected():
    return "Basic Auth: Access Granted"

# JWT Authentication

@app.route('/login', methods=['POST'])
def login():
    data = request.json
    username = data.get('username')
    password = data.get('password')
    if not username or not password:
        return jsonify({"error": "Username and password are required"}), 400
    user = users.get(username)
    if not user or not check_password_hash(user['password'], password):
        return jsonify({"error": "Invalid username or password"}), 401
    access_token = create_access_token(identity=username, additional_claims={"role": user['role']})
    return jsonify(access_token=access_token)

@app.route('/jwt-protected')
@jwt_required()
def jwt_protected():
    return "JWT Auth: Access Granted"

# Role-based Access Control

@app.route('/admin-only')
@jwt_required()
def admin_only():
    claims = get_jwt_claims()
    if claims['role'] != 'admin':
        return jsonify({"error": "Admin access required"}), 403
    return "Admin Access: Granted"

if __name__ == '__main__':
    app.run(debug=True)
