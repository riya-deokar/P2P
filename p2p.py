from flask import Flask, request, jsonify
import sqlite3
import os

app = Flask(__name__)

# Database setup
DATABASE = 'p2p_messaging.db'

def get_db():
    conn = sqlite3.connect(DATABASE)
    return conn

def init_db():
    db = get_db()
    cursor = db.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS messages (
            id INTEGER PRIMARY KEY,
            from_user TEXT,
            to_user TEXT,
            message TEXT,
            timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
        )
    ''')
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            username TEXT PRIMARY KEY,
            ip_address TEXT
        )
    ''')
    db.commit()
    db.close()
    print("Database initialized and tables created.")

@app.route('/')
def index():
    return "P2P Messaging App Running!"

@app.route('/register', methods=['POST'])
def register():
    """Register or update a user in the system."""
    username = request.json['username']
    ip_address = request.json['ip_address']
    db = get_db()
    cursor = db.cursor()
    cursor.execute('INSERT OR REPLACE INTO users (username, ip_address) VALUES (?, ?)', (username, ip_address))
    db.commit()
    return jsonify({"message": "User registered successfully"}), 200

# New endpoint for sending messages
@app.route('/send_message', methods=['POST'])
def send_message():
    from_user = request.json.get('from_user')
    to_user = request.json.get('to_user')
    message = request.json.get('message')
    if not from_user or not to_user or not message:
        return jsonify({"error": "Missing data for from_user, to_user, or message"}), 400

    db = get_db()
    cursor = db.cursor()
    cursor.execute('INSERT INTO messages (from_user, to_user, message) VALUES (?, ?, ?)',
                   (from_user, to_user, message))
    db.commit()
    return jsonify({"message": "Message sent successfully"}), 201

# New endpoint for retrieving messages
@app.route('/get_messages', methods=['GET'])
def get_messages():
    to_user = request.args.get('to_user')
    if not to_user:
        return jsonify({"error": "Missing 'to_user' parameter"}), 400

    db = get_db()
    cursor = db.cursor()
    cursor.execute('SELECT id, from_user, message, timestamp FROM messages WHERE to_user = ?', (to_user,))
    messages = cursor.fetchall()
    return jsonify({"messages": messages}), 200

if __name__ == '__main__':
    with app.app_context():
        init_db()  # Initialize the database
    app.run(debug=True)