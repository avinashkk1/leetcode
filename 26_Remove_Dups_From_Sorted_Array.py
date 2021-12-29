class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        n = len(nums)
        
        if n < 2:
            return n
        
        i = 1
        k = 1
        dup_count = 0
        
        while i < n:
            while i < n and nums[k - 1] == nums[i]:
                i += 1
                dup_count += 1
            
            if i < n:
                if i != k:
                    nums[k] = nums[i]
                i += 1
                k += 1
                
                    
        return n - dup_count
