class Solution:    
    
    def findUnion(self, a, b):
        set_a = set(a)
        set_b = set(b)
        union_set = set_a | set_b
        return list(union_set)