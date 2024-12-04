#!/usr/bin/env python3
"""simple flask template"""
from flask import Flask, render_template, request, g
from flask_babel import Babel

app = Flask(__name__)
babel = Babel(app)


class Config:
    """config file"""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app.config.from_object(Config)
users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}

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


def get_user():
    """get user"""
    usr_id = request.args.get('login_as')
    try:
        usr_id = int(usr_id)
        if usr_id in users:
            return users.get(usr_id)
    except:
        return None
    

@app.before_request
def before_request():
    """run befor others"""
    user = get_user()
    if user:
        g.user = user
    

if __name__ == '__main__':
    app.run(debug=True)
