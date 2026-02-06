from collections import Counter
class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        result=[]
        frequency = Counter(nums)
        for x,c in frequency.items():
            if c>len(nums)//3:
                result.append(x)
        return result
        
        