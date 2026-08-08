class Solution:
    def getSum(self, a: int, b: int) -> int:
        mask = 0xFFFFFFFF
        while b:
            t = (a & b) << 1
            a, b = (a ^ b) & mask, t & mask
        return a if a <= 0x7FFFFFFF else a - (1 << 32)