import redis
from app.core.config import settings

class Singleton(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]


class RedisClient():

    def __init__(self):
        self._conn = None
        self.pool = redis.ConnectionPool(
            host = settings.REDIS_SERVER,
            port = 6379,
            password = settings.REDIS_PASSWORD
        )

    @property
    def conn(self):
        if not hasattr(self, '_conn'):
            self.get_connection()
        return self._conn

    def get_connection(self):
        self._conn=redis.Redis(connection_pool = self.pool)
