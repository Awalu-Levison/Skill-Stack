from flask import Flask, render_template # type: ignore
app = Flask(__name__)
"""
Main application for Skill Stack E Learning Platform
Contains basic functions for the backend
and other neccessary dynamic functionality of the platform
"""

"""Home page"""
@app.route("/")
@app.route("/home")
def home():
    return render_template('index.html', title='Home')


"""About us age"""
@app.route("/about")
def about():
    return render_template('about.html', title='About')


"""Contact us page"""
@app.route("/contact")
def contact():
    return render_template('contact.html')

"""Learners dashboard"""
@app.route("/dashboard")
def dashboard():
    return render_template('dashboard.html')


if __name__ == "__main__":
    """run the application outside the development server"""
    app.run(host="0.0.0.0", debug=True)
