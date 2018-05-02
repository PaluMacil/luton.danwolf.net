from flask import g, Flask
import psycopg2
from psycopg2.extras import RealDictCursor
from app.db.repositories import ObservationRepo


class Db:
    def __init__(self, app: Flask):
        self._app = app
        self._conn = psycopg2.connect(app.config['DATABASE'], cursor_factory=RealDictCursor)

        self.observations = ObservationRepo(self._conn)

    def close(self):
        self._conn.close()

    def execute(self, command: str):
        self._conn.cursor().execute(command)
        self._conn.commit()

    def executeScript(self, script_name: str):
        with self._app.open_resource(f'../sql/{script_name}.sql', mode='r') as f:
            self.execute(f.read())

    @staticmethod
    def instance(app: Flask) -> 'Db':
        if 'db' not in g:
            g.db = Db(app)
        return g.db
