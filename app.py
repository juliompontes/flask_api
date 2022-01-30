import sqlite3
from flask import Flask, jsonify, render_template

app = Flask(__name__)

def get_db_connection():
    conn = sqlite3.connect('database.db')
    return conn

@app.route('/', methods=['GET'])
def index():
    conn = get_db_connection()
    salarys = conn.execute('SELECT * FROM salarys limit 3').fetchall()
    conn.close()
    return render_template('index.html', salarys=salarys)

@app.route('/data_sample', methods=['GET'])
def data_sample():
    conn = get_db_connection()
    first_salarys = conn.execute('SELECT * FROM salarys limit 10').fetchall()
    conn.close()
    return jsonify(first_salarys)

@app.route('/all_data', methods=['GET'])
def all_data():
    conn = get_db_connection()
    all_salarys = conn.execute('SELECT * FROM salarys').fetchall()
    conn.close()
    return jsonify(all_salarys)

if __name__ == '__main__':
    app.run(debug=True)