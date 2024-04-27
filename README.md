# Peer-to-Peer Messaging System

## Overview
This project is a basic implementation of a peer-to-peer (P2P) messaging system developed for a hackathon. It allows users to register themselves as available for communication, send messages to other users, and retrieve messages. The system is designed as a Flask-based web application using SQLite for data storage, handling user registrations, message sending, and message retrieval.

## Features

### Discovery
- **User Registration**: Users can make themselves discoverable to the system by registering their username and IP address. This is analogous to user discovery features in apps like Telegram or WhatsApp.

### Communication and Synchronization
- **Send Messages**: Users can send messages to other registered users. The system stores these messages in a SQLite database.
- **Retrieve Messages**: Users can retrieve messages sent to them by other users, ensuring that communication is possible in real time.

### MVP Achievement
The MVP of this project includes:
- **Discovery**: Implemented via a user registration system where users register their details to be discoverable.
- **Session Initiation**: Implicitly handled through the act of sending messages.
- **Communication and Synchronization**: Users can send and receive messages. Messages for offline users need to be handled if they are part of the extended requirements.

## Getting Started

### Prerequisites
- Python 3.8 or above
- Flask
- SQLite3

### Installation
1. Clone the repository: https://github.com/riya-deokar/P2P.git
2. Navigate to the project directory
3. Install the required packages: 
    ```bash
    pip install -r r.txt
    ```

### Running the Application
1. Start the Flask application:
    ```bash
    python p2p.py
    ```
2. The application will be available at `http://127.0.0.1:5000/`.

## Usage

### Registering a User
Send a POST request to `/register` with a JSON payload containing the username and IP address:
```bash
pcurl -X POST http://127.0.0.1:5000/register -H "Content-Type: application/json" -d '{"username": "Alice", "ip_address": "10.1.1.1"}'
```

### Sending a Message
Send a POST request to `/send_message` with a JSON payload containing the sender, receiver, and message:
```bash
curl -X POST http://127.0.0.1:5000/send_message -H "Content-Type: application/json" -d '{"from_user": "Alice", "to_user": "Bob", "message": "Hello, Bob!"}'
```
    
### Retrieving Messages
Send a GET request to `/get_messages` with the recipient's username as a query parameter:
```bash
curl 'http://127.0.0.1:5000/get_messages?to_user=Bob'
```