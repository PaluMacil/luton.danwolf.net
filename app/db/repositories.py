from typing import List, Optional
from app.db.models import *


class ObservationRepo:
    def __init__(self, db):
        self._db = db

    def one(self, id: int) -> Optional[Observation]:
        cur = self._db.cursor()
        cur.execute("""SELECT id, mac, ipv4, observation_type, observation_date 
                         FROM observations
                         WHERE id = %s
                           ORDER BY observation_date DESC
                        ;""", (id,))
        result = cur.fetchone()
        obs = Observation(result)
        return obs


    def all(self) -> List[Observation]:
        cur = self._db.cursor()
        cur.execute("""
          SELECT id, mac, ipv4, observation_type, observation_date 
          FROM observations
            ORDER BY observation_date DESC 
        ;""")
        result = cur.fetchall()
        obs: List[Observation] = [Observation(r) for r in result]

        return obs

    def get(self, query) -> List[Observation]:
        cur = self._db.cursor()
        cur.execute("""
          SELECT id, mac, ipv4, observation_type, observation_date 
          FROM observations
            ORDER BY observation_date DESC 
        ;""")
        result = cur.fetchall()
        return [Observation(r) for r in result]

    def add(self, mac: str, ipv4: str, observation_type: str, observation_date: datetime) -> Observation:
        cur = self._db.cursor()
        cur.execute("""
                  INSERT INTO observations 
                    (mac, ipv4, observation_type, observation_date)
                  VALUES 
                    (%s,%s,%s,%s)
                  RETURNING id, mac, ipv4, observation_type, observation_date
                ;""", (mac, ipv4, observation_type, observation_date,))
        result = cur.fetchone()
        obs = Observation(result)
        return obs
