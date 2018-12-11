from flask import Flask, render_template # We imported 2 seperate functions From 'flask'

app = Flask(__name__) # This variable will be referenced each time we define a route.
# Routes are the so called 'path' || 'Direction' the user is currently on in your app.
@app.route("/") # Default Route of Our App
def index():
    headline = "Welcome to Flask_Setup"
    return render_template("index.html", headline=headline)

@app.route("/gallery")
def view():
    return "<h1>welcome to gallery</h1>"