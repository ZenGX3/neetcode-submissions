class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        n = len(intervals)
        l = intervals.copy()
        l.sort()
        i = 0
        while i < len(l)-1:
            if l[i][1] >= l[i+1][0]:
                l[i] = [min(l[i][0], l[i+1][0]), max(l[i][1], l[i+1][1])]
                l.pop(i+1)
            else:
                i += 1
        return l

                