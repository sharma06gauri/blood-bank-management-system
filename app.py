# app.py
from flask import Flask, render_template, request, redirect, url_for
import mysql.connector

app = Flask(__name__)

# Configure your MySQL database connection
# Replace with your actual database credentials
db_config = {
    'host': 'localhost',
    'user': 'your_mysql_username',
    'password': 'your_mysql_password',
    'database': 'blood_bank'
}

def get_db_connection():
    """Establishes a connection to the MySQL database."""
    return mysql.connector.connect(**db_config)

@app.route('/')
def home():
    """Renders the home page with a list of available blood units."""
    try:
        conn = get_db_connection()
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM blood_stock")
        blood_stock = cursor.fetchall()
        cursor.close()
        conn.close()
        return render_template('index.html', blood_stock=blood_stock)
    except mysql.connector.Error as err:
        return f"Database error: {err}"

@app.route('/search', methods=['GET'])
def search_blood():
    """Handles blood search functionality."""
    blood_type = request.args.get('blood_type')
    try:
        conn = get_db_connection()
        cursor = conn.cursor(dictionary=True)
        query = "SELECT * FROM blood_stock WHERE blood_type = %s"
        cursor.execute(query, (blood_type,))
        results = cursor.fetchall()
        cursor.close()
        conn.close()
        return render_template('index.html', blood_stock=results, search_term=blood_type)
    except mysql.connector.Error as err:
        return f"Database error: {err}"

if __name__ == '__main__':
    app.run(debug=True)
