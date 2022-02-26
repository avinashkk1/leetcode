class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        targetDiff = None
        closestThreeSum = None
        
        
        n = len(nums)
        for i in range(n - 2):
            j, k = i + 1, n - 1
            
            while j < k:
                currSum = nums[i] + nums[j] + nums[k] 
                if currSum == target:
                    return target
                
                if targetDiff is None or abs(currSum - target) < targetDiff:
                    targetDiff = abs(currSum - target)
                    closestThreeSum = currSum
                
                if currSum < target:
                    j += 1
                else:
                    k -= 1
        
        return closestThreeSum
                    
                        
        