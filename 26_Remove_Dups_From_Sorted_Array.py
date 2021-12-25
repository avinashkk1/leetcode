class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        n = len(nums)
        if n < 2:
            return n
        
        k = 1
        for i in range(n):
            if nums[k - 1] != nums[i]:
                nums[k] = nums[i]
                k += 1
        
        return k
        