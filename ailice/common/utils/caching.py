
from functools import lru_cache

# Caching decorator for frequently accessed data
@lru_cache(maxsize=1024)
def cache_result(func):
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs)
    return wrapper

# Cache manager for vector database operations
class VectorCache:
    def __init__(self, size=10000):
        self.cache = lru_cache(maxsize=size)

    def get(self, key):
        return self.cache.get(key)

    def set(self, key, value):
        self.cache[key] = value

    def invalidate(self, key):
        self.cache.pop(key, None)

    def clear(self):
        self.cache.cache_clear()
