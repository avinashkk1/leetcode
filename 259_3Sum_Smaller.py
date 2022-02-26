class Solution:
    def threeSumSmaller(self, nums: List[int], target: int) -> int:
        n = len(nums)
        
        if n < 3:
            return 0
        
        nums.sort()
        
        count = 0
        for k in range(n):
            i, j = 0, k - 1
            while i < j:
                if nums[i] + nums[j] + nums[k] < target:
                    count += j - i
                    i += 1
                else:
                    j -= 1
        
        return count
        