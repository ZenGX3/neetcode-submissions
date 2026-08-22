class Solution:
    def mergeTriplets(self, tri: List[List[int]], t: List[int]) -> bool:
        o = set()
        for x in tri:
            if x[0] > t[0] or x[1] > t[1] or x[2] > t[2]:
                continue
            for i, v in enumerate(x):
                if v == t[i]:
                    o.add(i)
        return len(o) == 3
