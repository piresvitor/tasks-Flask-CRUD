from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return "Hello World!"

@app.route("/about")
def sobre():
    return "Pagina sobre"

if __name__ == "__main__":
    app.run(debug=True)
