# Python code for implementing the Web platform with RESTful API

from flask import Flask, request, jsonify
#from random_string_generator import generate_random_string

app = Flask(__name__)

# Dummy data for entities
users = [
    {"id": 1, "username": "user1@example.com", "password": "password1", "status": "active", "balance": 100},
    {"id": 2, "username": "user2@example.com", "password": "password2", "status": "active", "balance": 50}
]

operations = [
    {"id": 1, "type": "addition", "cost": 5},
    {"id": 2, "type": "subtraction", "cost": 5},
    {"id": 3, "type": "multiplication", "cost": 10},
    {"id": 4, "type": "division", "cost": 10},
    {"id": 5, "type": "square_root", "cost": 8},
    {"id": 6, "type": "random_string", "cost": 3}
]

records = []

@app.route('/calculate', methods=['POST'])
def calculate():
    data = request.get_json()
    user_id = data.get('user_id')
    operation_id = data.get('operation_id')
    
    user = next((user for user in users if user['id'] == user_id), None)
    operation = next((operation for operation in operations if operation['id'] == operation_id), None)
    
    if not user or not operation:
        return jsonify({"message": "User or operation not found"}), 404
    
    if user['balance'] < operation['cost']:
        return jsonify({"message": "Insufficient balance"}), 400
    
    # Perform operation
    # Deduct cost from user's balance
    user['balance'] -= operation['cost']
    
    # Record the operation
    record = {
        "id": len(records) + 1,
        "operation_id": operation_id,
        "user_id": user_id,
        "amount": operation['cost'],
        "user_balance": user['balance'],
        "operation_response": "Result of the operation",
        "date": "current_date"
    }
    records.append(record)
    
    return jsonify({"message": "Operation successful", "user_balance": user['balance']}), 200

if __name__ == '__main__':
    app.run(debug=True)



