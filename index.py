from flask import Flask, redirect,url_for

app = Flask(__name__)

@app.route("/")
def home():
    return "<h1>Homepage</h1>"

@app.route("/contacts")
def contacts():
    return "<h1>Contacts</h1>"

@app.route("/private")
def admin():
    return redirect(url_for("home"))

if __name__ == "__main__":
    app.run()