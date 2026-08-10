class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if "0" in [num1, num2]:
            return "0"
        f = [0] * (len(num1) + len(num2))
        num1, num2 = num1[::-1], num2[::-1]
        for i1 in range(len(num1)):
            for i2 in range(len(num2)):
                d = int(num1[i1]) * int(num2[i2])
                f[i1 + i2] += d
                f[i1 + i2 + 1] += f[i1 + i2] //10
                f[i1 + i2] = f[i1 + i2] % 10
        f, b = f[::-1], 0
        while b < len(f) and f[b] == 0:
            b += 1
        f = map(str, f[b:])
        return "".join(f)