class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        list1Dict = {}
        for i, ele in enumerate(list1):
            list1Dict[ele] = i
        
        indexSum = len(list1) + len(list2)
        ans = []
        for i, ele in enumerate(list2):
            if ele in list1Dict:
                currIndexSum = list1Dict[ele] + i
                if currIndexSum < indexSum:
                    ans = []
                    indexSum = currIndexSum
                    ans.append(ele)
                elif currIndexSum == indexSum:
                    ans.append(ele)
        
        return ans
                    
        
            