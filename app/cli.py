from flask import current_app
from flask.cli import with_appcontext
import click
from app.db import Db


@click.command('initdb')
@with_appcontext
def init_db() -> None:
    """Initializes the database."""
    db = Db.instance(current_app)
    db.executeScript('setup')
    print('Initialized the database.')