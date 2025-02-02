#!/usr/bin/env python3
"""simple flask template"""
from flask import Flask, render_template, request
from flask_babel import Babel

app = Flask(__name__)
babel = Babel(app)


class Config:
    """config file"""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app.config.from_object(Config)


@babel.localeselector
def get_locale():
    """get lang"""
    lang = request.args.get('locale')
    return lang if lang in Config.LANGUAGES \
        else request.accept_languages.best_match(Config.LANGUAGES)


@app.route('/')
def welcome_page() -> str:
    """hompage"""
    return render_template('4-index.html')


if __name__ == '__main__':
    app.run(debug=True)
