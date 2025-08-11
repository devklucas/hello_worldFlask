from flask import Flask, redirect

app = Flask(__name__)

@app.route("/CV12")
def hello_world():
    return "<h1>Olá mundo!<h1>"

if __name__ == "__main__":
    app.run(debug=True, port=5173)