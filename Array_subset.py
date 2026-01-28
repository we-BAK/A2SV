from collections import Counter

class Solution:
    def isSubset(self, a, b):
        pantry = Counter(a)
        
        for ingredient in b:
            if pantry[ingredient] > 0:
                pantry[ingredient] -= 1
            else:
                return False
        
        return True