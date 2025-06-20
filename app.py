from flask import Flask, request, jsonify, send_file, render_template_string
import json
from datetime import datetime
import os

app = Flask(__name__)

# 🔐 Log file path
LOG_FILE = "log.txt"

# 🟢 Page HTML avec bouton de téléchargement
HTML_PAGE = """
<!DOCTYPE html>
<html lang="fr">
<head>
  <meta charset="UTF-8" />
  <title>Page de Test - OSINT Passive</title>
</head>
<body>
  <h1>Bienvenue sur la page de test</h1>
  <p>Les données de votre appareil seront automatiquement collectées.</p>

  <form action="/download-log" method="get">
    <button type="submit" style="padding: 10px 20px; background-color: #007BFF; color: white; border: none; border-radius: 5px; cursor: pointer;">
      📥 Télécharger les logs
    </button>
  </form>
</body>
</html>
"""

# ✅ Affiche la page avec le bouton
@app.route("/")
def index():
    return render_template_string(HTML_PAGE)

# ✅ Route de réception des données
@app.route("/log", methods=["POST"])
def receive_log():
    data = request.json
    data["timestamp"] = datetime.utcnow().isoformat()

    with open(LOG_FILE, "a", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False)
        f.write("\n")

    return jsonify({"status": "success"}), 200

# ✅ Route de téléchargement du fichier log
@app.route("/download-log", methods=["GET"])
def download_log():
    if os.path.exists(LOG_FILE):
        return send_file(LOG_FILE, as_attachment=True, download_name="log.txt")
    else:
        return "Fichier log introuvable", 404

# ✅ Lancer l’app localement
if __name__ == "__main__":
    app.run(debug=True)