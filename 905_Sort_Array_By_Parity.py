class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        n = len(nums)
        even_pos = 0
        odd_pos = n - 1
        while even_pos < odd_pos:
            while even_pos < odd_pos and nums[even_pos] % 2 == 0:
                even_pos += 1
            while even_pos < odd_pos and nums[odd_pos] % 2 == 1:
                odd_pos -= 1
            if even_pos < odd_pos:
                nums[even_pos], nums[odd_pos] = nums[odd_pos], nums[even_pos]
                even_pos += 1
                odd_pos -= 1
        
        return nums
            
        