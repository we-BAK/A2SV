from collections import Counter

class Solution:
    def findDuplicates(self, nums: list[int]) -> list[int]:
        freq = Counter(nums)
        
        result = []
        for key, value in freq.items():
            if value >= 2: 
                result.append(key)
        
        return result