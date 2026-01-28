class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        n=len(nums)
        majority=(n//2)+1
        for num in nums:
            fre=nums.count(num)
            

        