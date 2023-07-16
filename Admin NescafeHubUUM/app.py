import mysql.connector
from datetime import datetime
from flask import Flask, render_template, jsonify
import mysql.connector
import matplotlib.pyplot as plt
from io import BytesIO
import base64

# MySQL database configuration
db_config = {
    'host': 'cctmcagenda2.mysql.database.azure.com',
    'port': 3306,
    'user': 'alif',
    'password': 'alep1234!',
    'database': 'nescafe'
}

app = Flask(__name__)


@app.route('/')
def login():


    return render_template('login.html')



@app.route('/dashboard')
def dashboard():
    # Query the database to get the coffee and quantity_sold columns
    connection = mysql.connector.connect(**db_config)
    cur = connection.cursor()
    cur.execute("SELECT coffee, quantity FROM bookings")
    results = cur.fetchall()

    coffees = ["classic", "cappuccino", "latte"]
    quantities = [0, 0, 0]  # Initialize quantities for Classic, Cappuccino, and Latte

    for result in results:
        coffee = result[0].lower()  # Convert to lowercase for case-insensitive comparison
        quantity_str = result[1]
        if coffee in coffees and quantity_str:
            index = coffees.index(coffee)
            # Extract individual quantities and update the total
            quantity_list = [int(qty.strip()) for qty in quantity_str.split(',') if qty.strip().isdigit()]
            quantities[index] += sum(quantity_list)

    cur.close()

    # Create a bar chart
    plt.bar(coffees, quantities)

    # Add labels and title
    plt.xlabel('Coffee Types')
    plt.ylabel('Quantities Sold')
    plt.title('Coffee Sales Dashboard')

    # Convert the plot to a base64-encoded image
    buffer = BytesIO()
    plt.savefig(buffer, format='png')
    buffer.seek(0)
    chart_data = base64.b64encode(buffer.getvalue()).decode()
    plt.close()

    return render_template('dashboard.html', coffees=coffees, quantities=quantities, chart_data=chart_data)





@app.route('/eventorder')
def eventorder():
    # Connect to the database
    connection = mysql.connector.connect(**db_config)
    cursor = connection.cursor()

    # Fetch the data from the database
    cursor.execute("SELECT id, first_name, last_name, event_name, location, coffee, quantity, appointment_date, appointment_time, phone, message FROM bookings")
    orders = cursor.fetchall()

    # Print the value of orders for debugging
    print(orders)

    # Close the database connection
    cursor.close()
    connection.close()
    return render_template('eventOrder.html', orders=orders)


@app.route('/forgotpassword')
def forgotpassword():
    return render_template('forgotPassword.html')


@app.route('/incomingorder')
def incomingorder():
    # Connect to the database
    connection = mysql.connector.connect(**db_config)
    cursor = connection.cursor()

    # Fetch the data from the database
    cursor.execute("SELECT id, first_name, location, phone, email_address, pickup_delivery, subtotal, total, payment_method, terms_conditions, delivery FROM orders")
    orders = cursor.fetchall()

    # Print the value of orders for debugging
    print(orders)

    # Close the database connection
    cursor.close()
    connection.close()
    return render_template('incomingOrder.html', orders=orders)


@app.route('/logout')
def logout():
    return render_template('logout.html')


@app.route('/menu')
def menu():
    return render_template('menu.html')


@app.route('/register')
def register():
    return render_template('register.html')


@app.route('/sales')
def sales():
    # Query the database to get the coffee and quantity_sold columns
    connection = mysql.connector.connect(**db_config)
    cur = connection.cursor()
    cur.execute("SELECT coffee, quantity FROM bookings")
    results = cur.fetchall()

    coffees = ["classic", "cappuccino", "latte"]
    quantities = [0, 0, 0]  # Initialize quantities for Classic, Cappuccino, and Latte

    for result in results:
        coffee = result[0].lower()  # Convert to lowercase for case-insensitive comparison
        quantity_str = result[1]
        if coffee in coffees and quantity_str:
            index = coffees.index(coffee)
            # Extract individual quantities and update the total
            quantity_list = [int(qty.strip()) for qty in quantity_str.split(',') if qty.strip().isdigit()]
            quantities[index] += sum(quantity_list)

    cur.close()

    # Create a bar chart
    plt.bar(coffees, quantities)

    # Add labels and title
    plt.xlabel('Coffee Types')
    plt.ylabel('Quantities Sold')
    plt.title('Coffee Sales Dashboard')

    # Convert the plot to a base64-encoded image
    buffer = BytesIO()
    plt.savefig(buffer, format='png')
    buffer.seek(0)
    chart_data = base64.b64encode(buffer.getvalue()).decode()
    plt.close()

    return render_template('sales.html', coffees=coffees, quantities=quantities, chart_data=chart_data)


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000, debug=False)