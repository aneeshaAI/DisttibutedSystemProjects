from flask import Flask, request, jsonify

app = Flask(__name__)

accounts = {"A": 1000, "B": 500}
processed_txns = set()  # Deduplication store

@app.route("/transfer", methods=["POST"])
def transfer():
    data = request.json
    txn_id = data["transaction_id"]
    from_acc = data["from_account"]
    to_acc = data["to_account"]
    amount = data["amount"]

    if txn_id in processed_txns:
        return jsonify({"status": "duplicate", "message": "Transaction already processed"}), 200

    # Non-idempotent operation: actual money transfer
    if accounts[from_acc] >= amount:
        accounts[from_acc] -= amount
        accounts[to_acc] += amount
        processed_txns.add(txn_id)
        return jsonify({"status": "success", "accounts": accounts}), 200
    else:
        return jsonify({"status": "failed", "message": "Insufficient funds"}), 400

if __name__ == "__main__":
    app.run(port=5000, debug=True)
