class Solution:
    def isValid(self, s: str) -> bool:
        st = []
        for x in s:
            try:
                if st[-1] == '[' and x == ']' or st[-1] == '{' and x == '}' or st[-1] == '(' and x == ')':
                    st.pop(-1)
                else:
                    st.append(x)
            except:
                st.append(x)
        print(st)
        return not bool(st)
        