class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        n = len(nums)
        for i in range(n):
            k = abs(nums[i])
            if nums[k - 1] > 0:
                nums[k - 1] = -1 * nums[k - 1]
        
        ans = []
        for i in range(n):
            if nums[i] > 0:
                ans.append(i + 1)
        
        return ans
            
            
                
                
            
        
        
    def findDisappearedNumbers1(self, nums: List[int]) -> List[int]:
        n = len(nums)
        
        i = 0
        while i < n:
            if nums[i] != i + 1:
                k = nums[i] - 1
                if nums[k] != nums[i]:
                    nums[i], nums[k] = nums[k], nums[i]
                else:
                    i += 1
            else:
                i += 1
        
        ans = []
        for i in range(n):
            if nums[i] != i + 1:
                ans.append(i + 1)
        
        return ans
            
            
        