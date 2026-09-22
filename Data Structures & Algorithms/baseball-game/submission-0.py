class Solution:
    def calPoints(self, ops: List[str]) -> int:
        st = []
        sm = 0
        for x in ops:
            if x == "+":
               a = int(st.pop())
               b = int(st.pop())
               c = a + b
               st.append(b)
               st.append(a)
               st.append(c)
            elif x == "D":
                st.append(int(st[-1])*2)
            elif x == "C":
                st.pop()
            else:
                st.append(x)
        while st:
            sm += int(st.pop())
        return sm
                