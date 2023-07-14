import mysql.connector
from datetime import datetime
from flask import Flask, render_template, request, session, redirect, url_for
import mysql.connector
# MySQL database configuration
db_config = {
    'host': 'cctmcagenda2.mysql.database.azure.com',
    'port': 3306,
    'user': 'alif',
    'password': 'alep1234!',
    'database': 'spa'
}

app = Flask(__name__)


@app.route('/')
def login():
    return render_template('login.html')

@app.route('/dashboard')
def dashboard():
    # Query the database to get the total number of rows
    connection = mysql.connector.connect(**db_config)
    cur = connection.cursor()
    cur.execute("SELECT COUNT(*) FROM nescafe")
    total_rows = cur.fetchone()[0]
    cur.close()

    return render_template('dashboard.html', total_rows=total_rows)



@app.route('/eventorder')
def eventorder():
    # Connect to the database
    connection = mysql.connector.connect(**db_config)
    cursor = connection.cursor()

    # Fetch the data from the database
    cursor.execute(
        "SELECT id, first_name, last_name, event_name, location, coffee, quantity, appointment_date, appointment_time, phone, message FROM nescafe")
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
    return render_template('incomingOrder.html')


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
    return render_template('sales.html')

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000, debug=False)
