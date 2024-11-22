from flask import Flask, abort, render_template
app = Flask(__name__)

@app.route("/")
def index():
   return render_template('index.html')

@app.route("/login")
def login():
    return render_template('login.html')

@app.route("/signup")
def signup():
    return render_template('signup.html')

@app.route("/home")
def home():
    return render_template('home.html')

@app.route("/passreset")
def passreset():
    return render_template('passreset.html')

@app.route('/force404')
def force404():
    abort(404)

@app.errorhandler(404)
def  page_not_found(error):
    return "Couldn't find the page you requested", 404

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug = True)