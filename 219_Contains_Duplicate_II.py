class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        numsSet = dict()
        for i in range(len(nums)):
            if nums[i] in numsSet:
                if abs(numsSet[nums[i]] - i) <= k:
                    return True
            numsSet[nums[i]] = i
        
        return False