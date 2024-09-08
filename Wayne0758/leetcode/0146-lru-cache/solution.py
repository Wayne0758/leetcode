class LRUCache:

    def __init__(self, capacity: int):
        self.hashmap = defaultdict()
        self.l = []
        self.capacity = capacity

    def get(self, key: int) -> int:
        if key not in self.hashmap.keys():
            return -1
        self.l.remove(key)
        self.l.append(key)
        return self.hashmap[key]

    def put(self, key: int, value: int) -> None:
        self.hashmap[key] = value
        
        if key in self.l:
            self.l.remove(key)
        self.l.append(key)
        if len(self.l)>self.capacity:
            lru = self.l.pop(0)
            del self.hashmap[lru]
            return None
        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
