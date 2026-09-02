"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        st = sorted([x.start for x in intervals])
        ed = sorted([x.end for x in intervals])
        f, c = 0, 0
        s, e = 0, 0
        while s < len(intervals):
            if st[s] < ed[e]:
                s += 1
                c += 1
            else:
                e += 1
                c -= 1
            f = max(f, c)
        return f
            