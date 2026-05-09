class Node:
    def __init__(self, key: int, val: int):
        self.key = key
        self.val = val
        self.left = None
        self.right = None

class LRUCache:
    def __init__(self, capacity: int):
        self.cache = {}
        self.oldest = Node(-1,-1)
        self.newest = Node(-1, -1)
        self.oldest.right = self.newest
        self.newest.left = self.oldest
        self.capacity = capacity
        
    def delete(self, node: Node) -> None:
        l = node.left
        r = node.right
        if l:
            l.right = r
        if r:
            r.left = l
        self.cache.pop(node.key)

    def insert_right(self, node: Node) -> None:
        mru = self.newest.left
        mru.right = node
        node.left, node.right = mru, self.newest
        self.newest.left = node
        self.cache[node.key] = node

    def get(self, key: int) -> int:
        cache = self.cache
        if key in cache:
            node = cache[key]
            self.delete(cache[key])
            self.insert_right(node)
            return cache[key].val
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        cache = self.cache

        if key in cache:
            self.get(key)
            node = cache[key]
            node.val = value
        else:
            node = Node(key, value)
            if len(cache) >= self.capacity:
                self.delete(self.oldest.right)
            self.insert_right(node)
            
        return
        
