from flask import flask
app = Flask(__name__)

@app.route("/")
def root():
    return "The default, 'root', route"

@app.route("/advwebtech/")
def index():
    return index.html
    
if __name__ == "__main__":
    app.run(host='0.0.0.0', debug = True)