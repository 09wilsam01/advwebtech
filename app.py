from flask import Flask, render_template
app = Flask ( __name__ )

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/home")
def home():
    return render_template('home.html')

@app.route("/19-22")
def nineteen():
    return render_template('19-22.html')

@app.route("/23")
def twentythree():
    return render_template('23.html')

@app.route("/24")
def twentyfour():
    return render_template('24.html')

@app.route("/aboutme")
def aboutme():
    return render_template('aboutme.html')

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)