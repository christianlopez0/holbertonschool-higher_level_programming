from flask import Flask, render_template, request
import json
import csv

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

# Route to display products
@app.route('/products')
def display_products():
    source = request.args.get('source')
    id_param = request.args.get('id')

    if source not in ['json', 'csv']:
        return render_template('product_display.html', error='Wrong source')

    if source == 'json':
        products = read_json_data()
    elif source == 'csv':
        products = read_csv_data()

    if id_param:
        filtered_products = [p for p in products if str(p['id']) == id_param]
        if not filtered_products:
            return render_template('product_display.html', error='Product not found')
        products = filtered_products

    return render_template('product_display.html', products=products)

if __name__ == '__main__':
    app.run(debug=True)
