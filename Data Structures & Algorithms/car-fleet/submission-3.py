class Solution:
    def carFleet(self, t: int, pos: List[int], spd: List[int]) -> int:
        p = [[p, s] for p, s in zip(pos, spd)]
        st = []
        for p, s in sorted(p)[::-1]:
            st.append((t-p)/s)
            if len(st) >= 2 and st[-1] <= st[-2]:
                st.pop()
        return len(st)  


        