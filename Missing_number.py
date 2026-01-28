class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n=len(nums)
        for m in range(n+1):
            if m not in nums:
                return m
       