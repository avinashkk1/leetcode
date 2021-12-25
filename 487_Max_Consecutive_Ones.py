class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        n = len(nums)
        left = right = maxConsecOnes = 0

        noOfZeros = 0
        while right < n:
            if nums[right] == 0:
                noOfZeros += 1
            
            while noOfZeros == 2:
                if nums[left] == 0:
                    noOfZeros -= 1
                left += 1
            
            maxConsecOnes = max(maxConsecOnes, right - left + 1)
            right += 1
        
        return maxConsecOnes