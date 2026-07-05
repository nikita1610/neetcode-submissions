class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ans = [0]*n
        i = 0
        j = n-1
        k = j
        while (i<=j):
            square_i = nums[i]*nums[i]
            square_j = nums[j]*nums[j]
            if square_i > square_j:
                ans[k] = square_i
                i+=1
            else:
                ans[k] = square_j
                j-=1
            k-=1
        return ans