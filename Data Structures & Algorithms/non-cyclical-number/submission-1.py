class Solution:
    def product(self, n):
        ans = 0
        while n > 0:
            digit = n%10
            ans+=digit*digit
            n = n//10
        return ans
       

    def isHappy(self, n: int) -> bool:
        visited = set()
        while n not in visited:
            visited.add(n)
            n = self.product(n)
            if n ==1 :
                return True
        return False