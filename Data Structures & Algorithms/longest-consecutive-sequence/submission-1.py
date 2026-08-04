class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums.sort()
        if nums == []:
            return 0
        else:
            d = {}
            c = 0
            for x in nums:
                if not d:
                    d[c] = [x]
                elif d:
                    if d[c][-1]+1 != x and d[c][-1] != x:
                        c += 1
                        d[c] = [x]
                    elif d[c][-1] == x:
                        continue
                    else:
                        d[c].append(x)
            for x in d:
                return len(max(d.values(), key=len))

            