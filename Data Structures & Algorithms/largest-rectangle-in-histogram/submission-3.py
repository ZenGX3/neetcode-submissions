class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        m = 0
        st = []
        for i, h in enumerate(heights):
            s = i
            while st and st[-1][-1] > h:
                ind, ht = st.pop()
                m = max(m, ht*(i - ind))
                s = ind
            st.append((s, h))
        for i, h in st:
            m = max(m, h*(len(heights) - i))
        return m
        
        