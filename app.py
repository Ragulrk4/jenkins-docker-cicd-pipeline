from flask import Flask

app = Flask("app")

@app.route("/")
def home():
    return "Hello from Ragul's CI/CD pipeline!"

@app.route("/health")
def health():
    return "OK"
