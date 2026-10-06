import os
from flask import Flask, jsonify

app = Flask(__name__)


@app.route("/")
def home():
    return jsonify(
        message="Hello from the CI/CD lab",
        version=os.getenv("APP_VERSION", "dev")
    )


@app.route("/healthz")
def healthz():
    return jsonify(status="ok")