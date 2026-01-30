from collections import Counter

class Solution:
    def isSubset(self, a, b):
        return Counter(b) <= Counter(a)
