from flask import Flask

app = Flask(__name__)


@app.route("/")
def hello_world():
    return "<h1>Soumya Ranjan Sahoo 1BM21IS410</h1>"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
