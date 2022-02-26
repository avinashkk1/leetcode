class Solution:
    def numberOfArrays(self, differences: List[int], lower: int, upper: int) -> int:
        n = len(differences)
        ans = upper - lower + 1
        d = differences
        
        
        (l, u) = (lower, upper)
        (p, q) = (l - d[0], u - d[0])
        
        if q < l or u < p:
            return 0
        (p, q) = (max(p, l), min(q, u))
        ans = min(ans, q - p + 1)
        
        # print(ans)
        
        for i in range(n):
            (p, q) = (p + d[i], q + d[i])
        
            if q < l or u < p:
                return 0
            (p, q) = (max(p, l), min(q, u))
            ans = min(ans, q - p + 1)
            # print(ans)
        
        return ans


        