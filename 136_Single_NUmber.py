class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        xorVal = 0
        for ele in nums:
            xorVal ^= ele
        return xorVal