class Solution:
    def insert(self, intervals: List[List[int]], ni: List[int]) -> List[List[int]]:

        i = 0

        while i < len(intervals):

            if ni[1] < intervals[i][0]:
                intervals.insert(i, ni)
                return intervals

            elif ni[0] > intervals[i][1]:
                i += 1

            else:
                ni = [
                    min(ni[0], intervals[i][0]),
                    max(ni[1], intervals[i][1])
                ]
                intervals.pop(i)

        intervals.append(ni)
        return intervals