#!/usr/bin/env python3
"""simple flask template"""
from flask import Flask, render_template, Flask-babel
from flask_babel import Babel

app = Flask(__name__)
babel = Babel(app)


class Config:
    """config file"""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'

app.config.from_object(Config)

@app.route('/')
def welcome_page() -> str:
    """hompage"""
    return render_template('0-index.html')


if __name__ == '__main__':
    app.run(debug=True)
