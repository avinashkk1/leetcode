class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        n = len(nums)
        
        if n < 4:
            return []
        
        nums.sort()
        
        ans = set()
        for l in range(n):
            for k in range(l):
                i, j = 0, k - 1
                while i < j:
                    currSum = nums[i] + nums[j] + nums[k] + nums[l]
                    if currSum == target:
                        ans.add((nums[i], nums[j], nums[k], nums[l]))
                        i += 1
                    elif currSum < target:
                        i += 1
                    else:
                        j -= 1
        
        return [list(eles) for eles in ans]
                        
                        
        
        
        