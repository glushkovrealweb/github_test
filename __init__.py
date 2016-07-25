from flask import Flask
import sys
app = Flask(__name__)
@app.route("/")
def hello():
    return "123"
if __name__ == "__main__":
    app.run()