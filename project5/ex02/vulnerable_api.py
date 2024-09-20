from flask import Flask, request, jsonify
import os

app = Flask(__name__)

users = {
    1: {"id": 1, "username": "user1", "role": "admin", "salary": 5000},
    2: {"id": 2, "username": "user2", "role": "user", "salary": 3000},
}

@app.route('/users/<int:user_id>', methods=['GET', 'PATCH'])
def get_user(user_id):
    user = users.get(user_id)
    if not user:
        return jsonify({"error": "User not found"}), 404

    if request.method == 'PATCH':
        data = request.get_json()
        for key, value in data.items():
            if key in user:
                user[key] = value
        return jsonify(user)
    
    return jsonify(user)

@app.route('/debug', methods=['GET'])
def debug_info():

    debug_data = {
        "debug": True,
        "environment": dict(os.environ),
        "flask_config": app.config,
    }
    return jsonify(debug_data)

if __name__ == '__main__':
    app.run(debug=True)
