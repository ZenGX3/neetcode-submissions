class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = {}
        for x in strs:
            k = tuple(sorted(x))
            if k in d:
                d[k].append(x)
            else:
                d[k] = [x]
        return list(d.values())
