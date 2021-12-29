class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        n = len(arr)
        if n == 1:
            return
        
        last_index = n - 1
        i = 0
        j = n - 1
        
        while i <= last_index:
            if arr[i] == 0:
                if i == last_index:
                    arr[j] = 0
                    j -= 1
                last_index -= 1
            i += 1
        
        while j >= 0:
            if arr[last_index] != 0:
                arr[j] = arr[last_index]                
            else:
                arr[j] = 0
                j -= 1
                if j >= 0:
                    arr[j] = 0
            j -= 1
            last_index -= 1
        
        
        
        
        