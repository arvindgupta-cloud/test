import os
from flask import Flask

app = Flask(__name__)

# Home Page
@app.route('/')
def home():
    return "Welcome to my First Project 🚀"

# About Page
@app.route('/about')
def about():
    return "This is the About Page. This project is built using Flask."

# Contact Page
@app.route('/contact')
def contact():
    return "Contact us at: support@example.com"

# Shop Page
@app.route('/shop')
def shop():
    return "Welcome to the Shop Page!"

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 8080))
    app.run(host='0.0.0.0', port=port)
