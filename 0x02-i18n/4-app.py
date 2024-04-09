#!/usr/bin/env python3
"""Flask app module.
"""

from flask import Flask, render_template, request
from flask_babel import Babel

app = Flask(__name__)


class Config:
    """Babel Configuration."""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app.config.from_object(Config)
babel = Babel(app)


@babel.localeselector
def get_locale():
    """Method to select a language translation for the user."""
    locale_param = request.args.get('locale')
    if locale_param:
        if locale_param in app.config['LANGUAGES']:
            return locale_param
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route("/")
def index():
    """Index route"""
    return render_template('4-index.html')


if __name__ == "__main__":
    app.run()
