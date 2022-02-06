class Solution:
    def findFinalValue(self, nums: List[int], original: int) -> int:
        mySet = set(nums)
        while True:
            if original in mySet:
                mySet.remove(original)
                original *= 2
            else:
                return original