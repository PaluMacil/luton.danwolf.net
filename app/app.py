from flask import Flask, g
from app.views import observer
from app.config import init_config
from app.cli import init_db


def create_app() -> Flask:
    """create Flask app object and configure app global items (thread local is not yet available)."""
    app = Flask(__name__.split('.')[0])
    init_config(app)
    app.register_blueprint(observer)
    app.teardown_appcontext(close_db)
    app.cli.add_command(init_db)

    return app


def close_db(e=None) -> None:
    """Closes the database again at the end of the request."""
    db = g.pop('db', None)
    if db is not None:
        db.close()
