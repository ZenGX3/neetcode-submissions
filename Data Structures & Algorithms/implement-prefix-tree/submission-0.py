class Node:
    def __init__(self):
        self.chld = {}
        self.eow = False
class PrefixTree:
    def __init__(self):
        self.root = Node()

    def insert(self, word: str) -> None:
        cur = self.root
        for c in word:
            if c not in cur.chld:
                cur.chld[c] = Node()
            cur = cur.chld[c]
        cur.eow = True

    def search(self, word: str) -> bool:
        cur = self.root
        for c in word:
            if c not in cur.chld:
                return False
            cur = cur.chld[c]
        return cur.eow

    def startsWith(self, prefix: str) -> bool:
        cur = self.root
        for c in prefix:
            if c not in cur.chld:
                return False
            cur = cur.chld[c]
        return True
        