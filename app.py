from flask import Flask, request, jsonify
import os
import json
from datetime import datetime

app = Flask(__name__)

@app.route("/")
def index():
    return "Serveur Flask actif."

@app.route("/log", methods=["POST"])
def log_data():
    data = request.get_json()
    if data:
        # Affichage en live dans Railway Logs
        print("✅ Données reçues :", data)
        
        # Sauvegarde dans log.txt
        with open("log.txt", "a") as f:
            f.write(f"{datetime.now().isoformat()} - {json.dumps(data)}\n")
        return jsonify({"status": "OK"}), 200
    return jsonify({"error": "Aucune donnée reçue"}), 400

@app.route("/view-logs")
def view_logs():
    try:
        with open("log.txt", "r") as f:
            return f"<pre>{f.read()}</pre>"
    except FileNotFoundError:
        return "⚠️ Aucun fichier log.txt trouvé."

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
