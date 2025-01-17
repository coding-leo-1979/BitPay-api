from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# 더미 데이터
wallet_data = {
    "balance": 1000,
    "transaction": [
        {"time": "2025-01-10 10:30:00", "sender": "public123", "recipient": "1234567890", "amount": 100},
        {"time": "2025-01-12 14:00:00", "sender": "0987654321", "recipient": "public123", "amount": 200},
        {"time": "2025-01-12 14:00:00", "sender": "public123", "recipient": "1111111111", "amount": 200}
    ]
}

# 회원가입
@app.route('/signup', methods=['POST'])
def create_wallet():
    return jsonify({
        "public_key": "public123",
        "private_key": "private123"
    })

# 홈
@app.route('/home', methods=['POST'])
def home():
    data = request.json
    my_address = data.get("myAddress", "default_address")
    
    return jsonify(wallet_data)

if __name__ == '__main__':
    app.run(debug=True, port=5000)
