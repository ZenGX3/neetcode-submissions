import math
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        st = []
        s = ''
        for x in tokens:

            if x not in '+-/*':
                st.append(x)
            else:
                a = st.pop()
                b = st.pop()
                st.append(str(int(eval(f'{b}{x}{a}'))))
        return int(st[0])
        