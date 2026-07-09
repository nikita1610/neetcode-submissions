class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        ans = []
        stack = []
        hash_map = {}

        n = len(nums2)

        for i in range(n-1, -1 , -1):
            while stack:
                if stack[-1] > nums2[i]:
                    hash_map[nums2[i]] = stack[-1]
                    stack.append(nums2[i])
                    break
                else:
                    stack.pop()
            if not stack:
                hash_map[nums2[i]] = -1
                stack.append(nums2[i])
        for i in nums1:
            ans.append(hash_map[i])
        return ans
        