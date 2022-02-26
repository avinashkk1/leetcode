import collections

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        m = len(s)
        n = len(t)
        
        if m != n:
            return False
        
        return collections.Counter(s) == collections.Counter(t)
        
        