from flask import Flask, request, jsonify

app = Flask(__name__)

tasks = []  # Persistent state during server runtime

@app.route("/add", methods=["POST"])
def add_task():
    data = request.json
    tasks.append(data["task"])
    return jsonify({"tasks": tasks})

@app.route("/list", methods=["GET"])
def list_tasks():
    return jsonify({"tasks": tasks})

if __name__ == "__main__":
    app.run(port=5000)
