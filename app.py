from flask import Flask, redirect

app = Flask(__name__)

@app.route("/CV12")
def hello_world():
    return redirect("https://www.youtube.com/watch?v=mWBNI1cS0jg&t=19s")

if __name__ == "__main__":
    app.run(debug=True, port=5173)