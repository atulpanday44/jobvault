import redis

class Cache:
    def __init__(self, host='localhost', port=6379, db=0):
        self.client = redis.StrictRedis(host=host, port=port, db=db)

    def set(self, key, value, ex=None):
        """Set a value in the cache."""
        self.client.set(key, value, ex=ex)

    def get(self, key):
        """Get a value from the cache."""
        return self.client.get(key)

    def delete(self, key):
        """Delete a value from the cache."""
        self.client.delete(key)