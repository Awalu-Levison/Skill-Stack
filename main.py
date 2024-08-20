from flask import Flask, render_template
app = Flask(__name__)
"""
Main application for Skill Stack E Learning Platform
Contains basic functions for the backend
and other neccessary dynamic functionality of the platform
"""


"""Home page"""
@app.route("/home")
def home():
    return render_template('home.html')


"""About us age"""
@app.route("/about")
def about():
    return render_template('about.html')


"""Contact us page"""
@app.route("/contact")
def contact():
    return render_template('contact.html')


if __name__ == "__main__":
    app.run(debug=True)
