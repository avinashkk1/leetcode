

class RandomizedSet:

    def __init__(self):
        self.myDict = {}
        self.myList = []
        

    def insert(self, val: int) -> bool:
        if val in self.myDict:
            return False
        
        self.myDict[val] = len(self.myDict)
        self.myList.append(val)
        return True
            
        

    def remove(self, val: int) -> bool:
        if val in self.myDict:
            index = self.myDict[val]
            lastIndex = len(self.myList) - 1
            self.myList[index], self.myList[lastIndex] = self.myList[lastIndex], self.myList[index]
            self.myDict[self.myList[index]] = index
            self.myList.pop()
            self.myDict.pop(val)
            return True
        
        return False
        

    def getRandom(self) -> int:
        return random.choice(self.myList)
        
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()