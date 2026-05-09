class CacheNode:
    key = None
    val = None
    left = None
    right = None

    def __init__(self, key=-1, val=-1, left=None, right=None):
        self.key = key
        self.val = val
        self.left = left
        self.right = right    

class LRUCache:
    
    def __init__(self, capacity: int):
        # left = least recent
        self.cache = {}
        self.remaining = capacity
        self.oldest, self.newest = CacheNode(), CacheNode()
        self.oldest.right = self.newest
        self.newest.left = self.oldest

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        
        node = self.cache[key]
        if node.left:
            node.left.right = node.right
        if node.right:
            node.right.left = node.left

        node.right = self.newest
        node.left = self.newest.left
        self.newest.left.right = node
        self.newest.left = node
        return self.cache[key].val

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.get(key)
            node = self.cache[key]
            node.val = value
            return
        
        node = CacheNode(key, value)
        if self.remaining <= 0:
            # evict LRU
            self.cache.pop(self.oldest.right.key)
            if self.oldest.right.right:
                self.oldest.right.right.left = self.oldest
            self.oldest.right = self.oldest.right.right
            
        # put to the right
        node.left = self.newest.left
        node.right = self.newest
        self.cache[key] = node


        self.newest.left.right = node
        self.newest.left = node
        self.remaining -= 1





# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)