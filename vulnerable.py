import sqlite3
from flask import Flask, request

app = Flask(__name__)

@app.route('/user')
def get_user():
    user_id = request.args.get('id')
    
    # VULNERABLE: SQL Injection
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    
    # Direct string formatting - CodeQL will catch this!
    query = f"SELECT * FROM users WHERE id = '{user_id}'"
    cursor.execute(query)
    
    results = cursor.fetchall()
    conn.close()
    return str(results)

@app.route('/search')
def search():
    term = request.args.get('q')
    
    # Another vulnerable query using % formatting
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    query = "SELECT * FROM products WHERE name = '%s'" % term
    cursor.execute(query)
    
    results = cursor.fetchall()
    conn.close()
    return str(results)

if __name__ == '__main__':
    app.run()
