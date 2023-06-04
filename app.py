from flask import Flask
import random, string

app = Flask(__name__)


def generate_instance_id():
    return "".join(random.choices(string.ascii_letters + string.digits, k=25))


instance_id = generate_instance_id()


@app.route("/health")
def healthcheck():
    return {"status": "ok"}


@app.route("/api/v1/sum/<num1>/<num2>")
def sum(num1, num2):
    left = int(num1)
    right = int(num2)
    return {"result": str(left + right), "instance_id": instance_id}
