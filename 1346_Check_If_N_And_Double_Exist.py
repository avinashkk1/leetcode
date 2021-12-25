class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        arr_set = set()
        n = len(arr)
        
        for i in range(n):
            if arr[i] * 2 in arr_set or (arr[i] % 2 == 0 and arr[i] //2 in arr_set):
                return True
            
            arr_set.add(arr[i])
        
        return False
        