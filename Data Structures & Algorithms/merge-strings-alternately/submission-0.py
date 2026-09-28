class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        s1 = list(word1)[::-1]
        s2 = list(word2)[::-1]
        s = ""
        while s1 and s2:
            s += s1[-1]+s2[-1]
            s1.pop();s2.pop()
        if s1:
            s += "".join(s1[::-1])
        else:
            s += "".join(s2[::-1])
        return s