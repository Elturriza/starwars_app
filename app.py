from flask import Flask
from config import Config

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    from presentation.movies import movies_bp
    app.register_blueprint(movies_bp)

    return app