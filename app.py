from flask import Flask, render_template
app = Flask ( __name__ )

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/home")
def home():
    return render_template('home.html')

@app.route("/19-22")
def home():
    return render_template('19-22.html')

@app.route("/23")
def home():
    return render_template('23.html')

@app.route("/24")
def home():
    return render_template('24.html')

@app.route("/aboutme")
def home():
    return render_template('aboutme.html')

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug = True)