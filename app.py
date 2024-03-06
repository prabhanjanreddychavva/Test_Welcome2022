# app.py
from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def index():
    user_agent = request.headers.get('User-Agent')
    return f"Welcome to 2022! User Agent: {user_agent}"

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
