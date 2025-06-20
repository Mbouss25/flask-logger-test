from flask import Flask, request
import os

app = Flask(__name__)

@app.route("/")
def index():
    return "Serveur Flask actif."

@app.route("/log", methods=["POST"])
def log_data():
    data = request.json
    with open("log.txt", "a") as f:
        f.write(str(data) + "\n")
    return {"status": "OK"}, 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
