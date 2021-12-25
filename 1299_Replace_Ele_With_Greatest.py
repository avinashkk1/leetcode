class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        n = len(arr)
        if n == 1:
            arr[0] = -1
            return arr
        
        max_so_far = arr[n - 1]
        arr[n - 1] = -1
        for i in range(n - 2, -1, -1):
            curr_max = max_so_far
            max_so_far = max(max_so_far, arr[i])
            arr[i] = curr_max
        
        return arr
        
        