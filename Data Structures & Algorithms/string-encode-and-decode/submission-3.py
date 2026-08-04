class Solution:

    def encode(self, strs: List[str]) -> str:
        s = ""
        for x in strs:
            s += (x if x else "^")+"~"
        return s
    def decode(self, s: str) -> List[str]:
        return [x if x!="^" else "" for x in s.split("~")[0:-1]]
            
