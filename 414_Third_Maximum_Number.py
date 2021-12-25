class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        max1 = max2 = max3 = None
        
        for ele in nums:
            if ele in (max1, max2, max3):
                continue
                
            if max1 is None or max1 < ele:
                max3 = max2
                max2 = max1
                max1 = ele
            elif max2 is None or max2 < ele:
                max3 = max2
                max2 = ele
            elif max3 is None or max3 < ele:
                max3 = ele
        
        if max3 is None:
            return max1
        return max3
                
                
                
                
        
    def thirdMax1(self, nums: List[int]) -> int:
        maxSet = set()
        for ele in nums:
            maxSet.add(ele)
            if len(maxSet) > 3:
                maxSet.remove(min(maxSet))
        
        if len(maxSet) == 3:
            return min(maxSet)
        return max(maxSet)
        
                    
                
                
            
        