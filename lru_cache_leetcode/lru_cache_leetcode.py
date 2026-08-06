import os


class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.elems = 0
        self.cache = {}
        self.mru_list = []
         
    def update_list(self, key):
        self.mru_list.remove(key)
        self.mru_list.append(key)

    def get(self, key: int) -> int:
        
        if not key in self.cache:
            return -1
        
        self.update_list(key)
        return self.cache[key]
        

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.cache[key] = value
            self.update_list(key)
            return 

        if self.elems == self.capacity:
            self.cache.pop(self.mru_list[0], None)
            self.mru_list.remove(self.mru_list[0])
            self.elems -= 1

        self.cache[key] = value
        self.mru_list.append(key)
        self.elems += 1
        

lru = LRUCache(2)
lru.put(1, 1)
lru.put(2, 2)
print(lru.get(1))
lru.put(3, 3)
print(lru.get(2))
lru.put(4, 4)
print(lru.get(1))
print(lru.get(3))
print(lru.get(4))

