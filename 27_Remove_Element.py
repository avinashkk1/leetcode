class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        i = 0
        n = len(nums)
        j = n - 1
        count = 0
        
        while i <= j:
            while i <= j and nums[i] != val:
                i += 1
            while j >= i and nums[j] == val:
                count += 1
                j -= 1
            if i <= j:
                nums[i] = nums[j]
                i += 1
                j -= 1
                count += 1
        
        return n - count
                
        