class Solution:
    def isAlnum(self, char):
        return (
            ord('A') <= ord(char) <= ord('Z') or
            ord('a') <= ord(char) <= ord('z') or
            ord('0') <= ord(char) <= ord('9')
        )
    def isPalindrome(self, s: str) -> bool:
        new_s = ""
        for i in s:
            if self.isAlnum(i):
                new_s+=i.lower()
        l = 0
        r = len(new_s)-1
        while l < r:
            if new_s[l]!=new_s[r]:
                return False
            l+=1
            r-=1
        return True