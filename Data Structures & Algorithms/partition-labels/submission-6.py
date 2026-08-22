class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        l = list(s)
        o = set()
        l1 = []
        c = 0

        for i, x in enumerate(s):
            o.add(x)
            c += 1

            if all(ch not in l[i+1:] for ch in o):
                l1.append(c)
                c = 0
                o = set()

        return l1