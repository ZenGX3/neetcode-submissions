class Solution:
    def convertToTitle(self, cn: int) -> str:
        if cn == 0:
            return ""
        cn -= 1
        return self.convertToTitle(cn//26)+chr(65+cn%26)
            