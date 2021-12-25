class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        i = 0
        n = len(nums)
        j = n - 1
        ans = [0] * n
        k = n - 1
        
        while i <= j:
            if abs(nums[i]) < abs(nums[j]):
                ans[k] = nums[j] * nums[j]
                j -= 1
            else:
                ans[k] = nums[i] * nums[i]
                i += 1
            k -= 1
        
        return ans
            
        