class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        lf, rg = 0, len(matrix)-1
        def bs(ls):
            l = 0
            r = len(ls) - 1
            while l <= r:
                mid = (l + r)//2
                if ls[mid] < target:
                    l = mid + 1
                elif ls[mid] > target:
                    r = mid - 1
                elif ls[mid] == target:
                    return True 
            return False
        while lf <= rg:
            mid = (lf + rg)//2
            if target < matrix[mid][0]:
                rg = mid - 1
            elif target > matrix[mid][-1]:
                lf = mid + 1
            else:
                return bs(matrix[mid])
        return False
