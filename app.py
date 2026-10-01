from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/status")
def verificar_status():
    return jsonify({
        "aplicacao": "Monitor DevOps",
        "status": "online"
    })

@app.route("/health")
def verificar_saude():
    return jsonify({
        "status": "healthy"
    }), 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)