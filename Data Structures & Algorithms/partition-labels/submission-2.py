class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        l = list(s)
        o = set()
        l1 = []
        c = 0
        while l:
            x = l.pop(0)
            o.add(x)
            c += 1
            if all(ch not in l for ch in o):
                l1.append(c)
                c = 0
                o = set()
        return l1
        
