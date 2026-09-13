class Node:
    def __init__(self, k, v):
        self.k, self.v = k, v
        self.prev = self.next = None
class LRUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.cache = {}
        self.l, self.r = Node(0, 0), Node(0, 0)
        self.l.next, self.r.prev = self.r, self.l
    
    def remove(self, node):
        p, n = node.prev, node.next
        p.next, n.prev = n, p
    def insert(self, node):
        p, n = self.r.prev, self.r
        p.next = n.prev = node
        node.next, node.prev = n, p

    def get(self, k: int) -> int:
        if k in self.cache:
            self.remove(self.cache[k])
            self.insert(self.cache[k])
            return self.cache[k].v
        return -1

    def put(self, k: int, v: int) -> None:
        if k in self.cache:
            self.remove(self.cache[k])
        self.cache[k] = Node(k, v)
        self.insert(self.cache[k])
        if len(self.cache) > self.cap:
            lru = self.l.next
            self.remove(lru)
            del self.cache[lru.k]

