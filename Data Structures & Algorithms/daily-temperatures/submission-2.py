class Solution:
    def dailyTemperatures(self, nums: List[int]) -> List[int]:
        ans = [0]*len(nums)
        stack = []
        n = len(nums)
        for i in range(n-1, -1 , -1):
            while stack:
                if nums[stack[-1]] > nums[i]:
                    ans[i] = stack[-1]-i
                    stack.append(i)
                    break
                else:
                    stack.pop()
            if not stack:
                stack.append(i)
        return ans
        