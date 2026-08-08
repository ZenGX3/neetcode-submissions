class Solution:
    def reverse(self, x: int) -> int:
        imin = -2147483648
        imax = 2147483647

        f = 0
        while x:
            d = int(math.fmod(x, 10))
            x = int(x / 10)
            if f > imax // 10 or (f == imax // 10 and d >= imax % 10):
                return 0
            if f < imin // 10 or (f == imin // 10 and d <= imin % 10):
                return 0
            f = (f * 10) + d
        return f 
        