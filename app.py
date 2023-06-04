from flask import Flask

app = Flask(__name__)

@app.route("/health")
def healthcheck():
    return {
        "status": "ok"
    }
