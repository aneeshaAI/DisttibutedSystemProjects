# Currency Converter API
from flask import Flask, request, jsonify

app = Flask(__name__)

exchange_rates = {"USD": 1, "INR": 83, "EUR": 0.9}

@app.route("/convert", methods=["GET"])
def convert():
    amount = float(request.args.get("amount"))
    from_curr = request.args.get("from")
    to_curr = request.args.get("to")
    converted = amount / exchange_rates[from_curr] * exchange_rates[to_curr]
    return jsonify({"converted_amount": converted})

if __name__ == "__main__":
    app.run(port=5000)
