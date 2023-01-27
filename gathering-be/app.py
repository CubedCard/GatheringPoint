from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/')
def index():
    return "Welcome to the RESTful API"

@app.route('/users', methods=['GET'])
def get_users():
    # Code to retrieve user data from a database
    users = [{'id': 1, 'name': 'John Doe'}, {'id': 2, 'name': 'Jane Doe'}]
    return jsonify(users)

if __name__ == '__main__':
    app.run(debug=True)


