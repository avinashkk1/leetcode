class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        n = len(nums)
        
        if n == 0:
            return 0
        
        if n == 1:
            if nums[0] == val:
                return 0
            return 1
        
        i = 0
        j = n - 1
        count = 0
        while i <= j:
            while i <= j and nums[i] != val:
                i += 1
            while i <= j and nums[j] == val:
                j -= 1
                count += 1
            if i <= j:
                nums[i] = nums[j]
                i += 1
                j -= 1
                count += 1
        
        return n - count
                
        