class Solution:
    def repeatedStringMatch(self, a: str, b: str) -> int:
        if b is None:
            return 0
        
        orig_a = a

        count = 1
        while len(a) < len(b):
            a += orig_a
            count += 1
        
        if b in a:
            return count
        
        a += orig_a
        count += 1

        if b in a:
            return count
        
        return -1
        