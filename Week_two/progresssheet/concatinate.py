class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        y=len(nums)
        for i in range(y):
            nums.append(nums[i])
        return nums