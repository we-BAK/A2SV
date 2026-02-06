class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        count=0
        if sorted(s1)==sorted(s2):

            for i in range(len(s1)):
                if s1[i]!=s2[i]:
                    count+=1
            if count>2:
                return False
            return True
        else:
            return False