import getpass, os
from flask import Flask


def init_config(app: Flask):
    user = getpass.getuser()
    app.config['DATABASE'] = os.environ.get('DATABASE') or f'user={user}'
