class Node:
    def __init__(self):
        self.d = {}
        self.eow = False

class WordDictionary:
    def __init__(self):
        self.root = Node()

    def addWord(self, word: str) -> None:
        cur = self.root
        for c in word:
            if c not in cur.d:
                cur.d[c] = Node()
            cur = cur.d[c]
        cur.eow = True

    def search(self, word: str) -> bool:
        def dfs(ind, rt):
            cur = rt

            for i in range(ind, len(word)):
                c = word[i]
                if c == ".":
                    for chld in cur.d.values():
                        if dfs(i + 1, chld):
                            return True
                    return False
                else:
                    if c not in cur.d:
                        return False
                    cur = cur.d[c]
            return cur.eow
        return dfs(0, self.root)
