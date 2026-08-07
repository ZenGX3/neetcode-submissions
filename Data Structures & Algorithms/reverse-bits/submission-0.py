class Solution:
    def reverseBits(self, n: int) -> int:
        f = 0
        for i in range(32):
            b = (n >> i) & 1
            f |= (b << (31 - i))
        return f