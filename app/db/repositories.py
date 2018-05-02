from typing import List, Optional
from app.db.models import *


class ObservationRepo:
    def __init__(self, conn):
        self._conn = conn

    def one(self, id: int) -> Optional[Observation]:
        cur = self._conn.cursor()
        cur.execute("""SELECT id, mac, ipv4, observation_type, observation_date 
                         FROM observations
                         WHERE id = %s
                           ORDER BY observation_date DESC
                        ;""", (id,))
        result = cur.fetchone()
        obs = Observation(result)
        return obs


    def all(self) -> List[Observation]:
        cur = self._conn.cursor()
        cur.execute("""
          SELECT id, mac, ipv4, observation_type, observation_date 
          FROM observations
            ORDER BY observation_date DESC 
        ;""")
        result = cur.fetchall()
        obs: List[Observation] = [Observation(r) for r in result]

        return obs

    def get(self, query) -> List[Observation]:
        cur = self._conn.cursor()
        cur.execute("""
          SELECT id, mac, ipv4, observation_type, observation_date 
          FROM observations
            ORDER BY observation_date DESC 
        ;""")
        result = cur.fetchall()
        return [Observation(r) for r in result]
