class Solution:
    def isPalindrome(self, s, i, j):
        while i < j:
            if s[i]!=s[j]:
                return False
            i+=1
            j-=1
        return True
    def validPalindrome(self, s: str) -> bool:
        start = 0 
        end = len(s)-1
        while start < end:
            if s[start]==s[end]:
                start+=1
                end-=1
            else:
                return (
                    self.isPalindrome(s, start+1, end) or
                    self.isPalindrome(s, start, end-1)
                )
        return True
        