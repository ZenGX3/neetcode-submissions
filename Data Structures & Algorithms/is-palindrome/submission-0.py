class Solution:
    def isPalindrome(self, s: str) -> bool:
        l = [x.lower() for x in s if x.isalpha() or x.isdigit()]
        return l[:len(l)//2] == l[(len(l)//2)+(len(l)%2):][::-1]