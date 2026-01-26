class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        n=0
        common_prefix=[]
        prefix =strs[0] 
        for t in strs[1:]:  
            while not t.startswith(prefix):     
              prefix=prefix[:-1]
        return prefix