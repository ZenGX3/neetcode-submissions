class Solution:
    def sortArray(self, arr: List[int]) -> List[int]:
        if len(arr) <= 1:
            return arr

        mid = len(arr) // 2
        left = self.sortArray(arr[:mid])
        right = self.sortArray(arr[mid:])

        return self.merge(left, right)


    def merge(self, a, b):
        res = []
        i = j = 0

        while i < len(a) and j < len(b):
            if a[i] <= b[j]:
                res.append(a[i])
                i += 1
            else:
                res.append(b[j])
                j += 1

        res.extend(a[i:])
        res.extend(b[j:])
        return res