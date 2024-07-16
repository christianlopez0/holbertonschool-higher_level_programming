from flask import Flask, render_template, request
import json
import csv
import sqlite3

app = Flask(__name__)

# Function to read JSON data from file
def read_json_data():
    with open('products.json', 'r') as json_file:
        data = json.load(json_file)
    return data

# Function to read CSV data from file
def read_csv_data():
    products = []
    with open('products.csv', 'r', newline='') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            products.append({
                'id': int(row['id']),
                'name': row['name'],
                'category': row['category'],
                'price': float(row['price'])
            })
    return products

# Function to fetch data from SQLite database
def read_sql_data():
    conn = sqlite3.connect('products.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM Products')
    products = cursor.fetchall()
    conn.close()

    # Convert fetched data into list of dictionaries
    products_list = []
    for product in products:
        products_list.append({
            'id': product[0],
            'name': product[1],
            'category': product[2],
            'price': float(product[3])
        })
    
    return products_list

# Route to display products
@app.route('/products')
def display_products():
    source = request.args.get('source')
    id_param = request.args.get('id')

    if source not in ['json', 'csv', 'sql']:
        return render_template('product_display.html', error='Wrong source')

    try:
        if source == 'json':
            products = read_json_data()
        elif source == 'csv':
            products = read_csv_data()
        elif source == 'sql':
            products = read_sql_data()
    except Exception as e:
        return render_template('product_display.html', error=f'Database error: {str(e)}')

    if id_param:
        filtered_products = [p for p in products if str(p['id']) == id_param]
        if not filtered_products:
            return render_template('product_display.html', error='Product not found')
        products = filtered_products

    return render_template('product_display.html', products=products)

if __name__ == '__main__':
    app.run(debug=True)
