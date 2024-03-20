# VinyRecordCollectorAPI.py

# This Python program implements a RESTful API for vinyl record collectors. The API allows users to store, manage, 
# and interact with details about their vinyl records.

# Users can register, log in, and perform CRUD (Create, Read, Update, Delete) operations on their records. Additionally, they can interact with other users, search for records, and view comments.

# The purpose of this API is to provide a centralized platform for vinyl collectors to organize and share information about their collections by offering a user-friendly interface 
# and robust functionality, the API aims to streamline the process of cataloging records, facilitating interactions between collectors.

# This API is implemented using Flask, a lightweight and flexible web framework for Python providing the necessary tools and libraries to build web applications and APIs quickly and efficiently. 

# The API endpoints are designed following RESTful principles, with each endpoint corresponding to a specific resource and operation. 

# Author: Andrea Cignoni


from flask import Flask, request, jsonify, make_response

app = Flask(__name__)

# Users database:
users = []

# Records database: 
records = []

# Endpoint to provide basic information about the API
@app.route('/')
def index():
     return """
    <h1>Welcome to the Vynil Collector API</h1>
    <p>Are you registered yet? </p>
    <ul>
        <li><a href="/option1">Register</a></li>
    <p>Otherwise: </p>
        <li><a href="/option2">Login</a></li>
    </ul>
    """

# Endpoint for user registration
@app.route('/Register', methods=['POST'])
def register():
    data = request.json
    # Implement user registration logic
    # Return appropriate response

# Endpoint for user login
@app.route('/Login', methods=['POST'])
def login():
    data = request.json
    # Implement user login logic
    # Return appropriate response

# Endpoint to create a new record
@app.route('/records/new', methods=['POST'])
def create_record():
    data = request.json
    # Authenticate the user (e.g., verify JWT token)
    # Validate input data
    # Assign a unique ID to the record
    # Associate the record with the authenticated user
    # Store the record information in the database
    # Return a success message or appropriate response

# Endpoint to get a specific vinyl record by ID
@app.route('/records/<int:record_id>', methods=['GET'])
def get_record(record_id):
    record = next((record for record in records if record['id'] == record_id), None)
    if record:
        return jsonify(record)
    else:
        return jsonify({"error": "Record not found"}), 404


# Endpoint to update an existing vinyl record by ID
@app.route('/records/<int:record_id>', methods=['PUT'])
def update_record(record_id):
    record = next((record for record in records if record['id'] == record_id), None)
    if record:
        data = request.json
        record.update(data)
        return jsonify({"message": "Record updated successfully", "record": record})
    else:
        return jsonify({"error": "Record not found"}), 404

# Endpoint to delete a vinyl record by ID
@app.route('/records/<int:record_id>', methods=['DELETE'])
def delete_record(record_id):
    global records
    records = [record for record in records if record['id'] != record_id]
    return jsonify({"message": "Record deleted successfully"})

if __name__ == '__main__':
    app.run(debug=True)

''''''''''
CREATE TABLE users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(50) UNIQUE NOT NULL,
    password_hash VARCHAR(128) NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE records (
    id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT,
    title VARCHAR(100) NOT NULL,
    label VARCHAR(100),
    year VARCHAR(4),
    condition VARCHAR(50),
    price DECIMAL(10, 2),
    date_of_purchase DATE,
    picture_url VARCHAR(255),
    description TEXT,
    FOREIGN KEY (user_id) REFERENCES users(id)
);
'''''