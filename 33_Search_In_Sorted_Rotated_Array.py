class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)
        
        if n == 1:
            return -1 if nums[0] != target else 0
        
        
        low, high = 0, n - 1
        
        while low <= high:
            mid = low + (high - low) // 2
            
            if target == nums[mid]:
                return mid
            
            if nums[low] <= nums[mid]:
                if nums[low] <= target < nums[mid]:
                    high = mid - 1
                else:
                    low = mid + 1
            else:
                if nums[mid] < target <= nums[high]:
                    low = mid + 1
                else:
                    high = mid - 1
                
        
        return -1
            