from datetime import datetime


class Model:
    def _map(self, record):
        fields=[a for a in dir(self) if not a.startswith('_') and not callable(getattr(self, a))]
        for f in fields:
            self.__setattr__(f, record.get(f))


class Observation(Model):
    def __init__(self, record = None):
        self.id : int
        self.mac : str
        self.ipv4 : str
        self.observation_type : str
        self.observation_date : datetime
        if record:
            self._map(record)
