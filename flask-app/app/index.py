from flask import Flask
background-image: url('http://www.pngmart.com/files/2/Mario-PNG-Image.png')
app = Flask(__name__)
@app.route("/")
def hello():
    return "Hello World from Python Flask...!"
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int("5000"), debug=True)