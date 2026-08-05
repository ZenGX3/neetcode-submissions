class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        st = []
        for x in tokens:

            if x not in '+-/*':
                st.append(x)
            else:
                a = int(st.pop())
                b = int(st.pop())
                if x == "+":
                    st.append(b + a)
                elif x == "-":
                    st.append(b - a)
                elif x == "*":
                    st.append(b * a)
                else:
                    st.append(int(b / a))
        return int(st[0])
        