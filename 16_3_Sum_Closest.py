class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        n = len(nums)
        
        nums.sort()
        threeSum = None
        
        for k in range(n):
            i, j = 0, k - 1
            while i < j:
                currSum = nums[i] + nums[j] + nums[k]
                if currSum == target:
                    return target
                
                if threeSum is None or abs(target - currSum) < abs(target - threeSum):
                    threeSum = currSum                        
                
                if currSum < target:
                    i += 1
                else:
                    j -= 1
                
        return threeSum
                    
                
        