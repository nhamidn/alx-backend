#!/usr/bin/env python3
"""Flask app module.
"""

from flask import Flask, render_template, request, g
from flask_babel import Babel, format_datetime
import pytz

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


@babel.timezoneselector
def get_timezone():
    """Gets the timezone for a web page."""
    timezone = request.args.get('timezone')
    if not timezone and g.user:
        timezone = g.user['timezone']
    try:
        return pytz.timezone(timezone).zone
    except pytz.exceptions.UnknownTimeZoneError:
        return app.config['BABEL_DEFAULT_TIMEZONE']


def get_user():
    """Retrieves a user based on a user id."""
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
    user = g.get('user', None)
    if user:
        user_locale = user.get('locale')
        if user_locale and user_locale in app.config['LANGUAGES']:
            return user_locale
    h_l = request.accept_languages.best_match(app.config['LANGUAGES'])
    if h_l:
        return h_l
    return app.config['BABEL_DEFAULT_LOCALE']


@app.before_request
def before_request():
    """Get user before each request's resolution."""
    g.user = get_user()


@app.route("/")
def index():
    """Index route"""
    g.time = format_datetime()
    return render_template('index.html')
    return request.accept_languages.best_match(app.config['LANGUAGES'])


if __name__ == "__main__":
    app.run()
