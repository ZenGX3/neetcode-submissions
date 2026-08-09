class Solution:
    def isHappy(self, n: int) -> bool:
        o = set()
        while n != 1:
            if n not in o:
                o.add(n)
                n = self.sosq(n)
            else:
                return False
        return True
    def sosq(self, n:int) -> int:
        s = 0
        while n:
            s += (n % 10)**2
            n //= 10
        return s
