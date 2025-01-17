from flask import Flask, jsonify, request
from flask_cors import CORS
import datetime

app = Flask(__name__)
CORS(app)

# 더미 데이터
wallet_data = {
    "balance": 1000,
    "transaction": [
        {"time": "2025-01-10 10:30:00", "sender": "public123", "recipient": "12345678901234567890123456789012345678901234567890", "amount": 100},
        {"time": "2025-01-12 14:00:00", "sender": "12345678901234567890123456789012345678901234567890", "recipient": "public123", "amount": 200},
        {"time": "2025-01-10 10:30:00", "sender": "public123", "recipient": "12345678901234567890123456789012345678901234567890", "amount": 100},
        {"time": "2025-01-12 14:00:00", "sender": "12345678901234567890123456789012345678901234567890", "recipient": "public123", "amount": 200},
        {"time": "2025-01-12 14:00:00", "sender": "public123", "recipient": "12345678901234567890123456789012345678901234567890", "amount": 200}
    ]
}

# 더미 데이터
wallet_data_all = {
    "balance": 1000,
    "transaction": [
        {"time": "2025-01-10 10:30:00", "sender": "public123", "recipient": "12345678901234567890123456789012345678901234567890", "amount": 100},
        {"time": "2025-01-12 14:00:00", "sender": "12345678901234567890123456789012345678901234567890", "recipient": "public123", "amount": 200},
        {"time": "2025-01-10 10:30:00", "sender": "public123", "recipient": "12345678901234567890123456789012345678901234567890", "amount": 100},
        {"time": "2025-01-12 14:00:00", "sender": "12345678901234567890123456789012345678901234567890", "recipient": "public123", "amount": 200},
        {"time": "2025-01-10 10:30:00", "sender": "public123", "recipient": "12345678901234567890123456789012345678901234567890", "amount": 100},
        {"time": "2025-01-12 14:00:00", "sender": "12345678901234567890123456789012345678901234567890", "recipient": "public123", "amount": 200},
        {"time": "2025-01-10 10:30:00", "sender": "public123", "recipient": "12345678901234567890123456789012345678901234567890", "amount": 100},
        {"time": "2025-01-12 14:00:00", "sender": "12345678901234567890123456789012345678901234567890", "recipient": "public123", "amount": 200},
        {"time": "2025-01-10 10:30:00", "sender": "public123", "recipient": "12345678901234567890123456789012345678901234567890", "amount": 100},
        {"time": "2025-01-12 14:00:00", "sender": "12345678901234567890123456789012345678901234567890", "recipient": "public123", "amount": 200},
        {"time": "2025-01-10 10:30:00", "sender": "public123", "recipient": "12345678901234567890123456789012345678901234567890", "amount": 100},
        {"time": "2025-01-12 14:00:00", "sender": "12345678901234567890123456789012345678901234567890", "recipient": "public123", "amount": 200},
        {"time": "2025-01-10 10:30:00", "sender": "public123", "recipient": "12345678901234567890123456789012345678901234567890", "amount": 100},
        {"time": "2025-01-12 14:00:00", "sender": "12345678901234567890123456789012345678901234567890", "recipient": "public123", "amount": 200},
        {"time": "2025-01-10 10:30:00", "sender": "public123", "recipient": "12345678901234567890123456789012345678901234567890", "amount": 100},
        {"time": "2025-01-12 14:00:00", "sender": "12345678901234567890123456789012345678901234567890", "recipient": "public123", "amount": 200},
        {"time": "2025-01-10 10:30:00", "sender": "public123", "recipient": "12345678901234567890123456789012345678901234567890", "amount": 100},
        {"time": "2025-01-12 14:00:00", "sender": "12345678901234567890123456789012345678901234567890", "recipient": "public123", "amount": 200},
        {"time": "2025-01-10 10:30:00", "sender": "public123", "recipient": "12345678901234567890123456789012345678901234567890", "amount": 100},
        {"time": "2025-01-12 14:00:00", "sender": "12345678901234567890123456789012345678901234567890", "recipient": "public123", "amount": 200},
        {"time": "2025-01-12 14:00:00", "sender": "public123", "recipient": "12345678901234567890123456789012345678901234567890", "amount": 200}
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

# 지갑
@app.route('/wallet', methods=['POST'])
def wallet():
    data = request.json
    my_address = data.get("myAddress", "default_address")
    
    return jsonify(wallet_data_all)

# 송금
@app.route('/send', methods=['POST'])
def send():
    data = request.json
    send_address = data.get("sendAddress")
    my_address = data.get("myAddress")
    private_key = data.get("privateKey")
    amount = data.get("amount")
    
    if not send_address or not my_address or not private_key or not amount:
        return jsonify({"error": "모든 필드를 입력해주세요."}), 400
        
    # 트랜잭션 추가
    new_transaction = {
        "time": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "sender": my_address,
        "recipient": send_address,
        "amount": amount
    }
    
    # 잔액 차감
    wallet_data_all['transaction'].insert(0, new_transaction)  # 더미 데이터 배열에 추가
    
    return jsonify({
        "message": "송금 완료",
        "transaction": new_transaction,
        "updated_balance": wallet_data_all['balance'],
        "updated_transactions": wallet_data_all['transaction']
    })

if __name__ == '__main__':
    app.run(debug=True, port=5000)
