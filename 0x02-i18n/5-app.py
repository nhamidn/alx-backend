#!/usr/bin/env python3
"""Flask app module.
"""

from flask import Flask, render_template, request, g
from flask_babel import Babel

app = Flask(__name__)
users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


class Config:
    """Babel Configuration."""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app.config.from_object(Config)
babel = Babel(app)


def get_user():
    user_id = request.args.get("login_as")
    if user_id is not None:
        try:
            user_id = int(user_id)
            return users.get(user_id)
        except ValueError:
            pass
    return None


@babel.localeselector
def get_locale():
    """Method to select a language translation for the user."""
    locale_param = request.args.get('locale')
    if locale_param:
        if locale_param in app.config['LANGUAGES']:
            return locale_param
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.before_request
def before_request():
    g.user = get_user()


@app.route("/")
def index():
    """Index route"""
    return render_template('5-index.html')


if __name__ == "__main__":
    app.run()
