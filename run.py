from flask import Flask
from src.api import api
from src.models.schemas import ma
from src.config import config
from flask_cors import CORS


def create_app() -> Flask:
    app = Flask(__name__)
    # CORS(app)
    cors = CORS(app, resources={r"/api/*": {"origins": "*"}})
    app.config.from_object(config["devConfig"])

    api.init_app(app)

    from src.models.Models import db
    db.init_app(app)
    ma.init_app(app)

    with app.app_context():
        db.create_all()
    return app

if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)
