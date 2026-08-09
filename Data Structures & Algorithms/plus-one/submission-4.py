class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        n = "".join(map(str, digits))
        return list(map(int, str(int(n)+1)))