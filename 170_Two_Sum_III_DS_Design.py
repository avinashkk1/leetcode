class TwoSum:

    def __init__(self):
        self.numDict = {}
        self.index = 0
        

    def add(self, number: int) -> None:
        if number in self.numDict:
            self.numDict[number].append(index)
        else:
            self.numDict[number] = [index]
        self.index += 1
        

    def find(self, value: int) -> bool:
        numDict = self.numDict
        for number, indexList in numDict.items():
            if (2 * number != value and value - number in numDict) or (2 * number == value and len(numDict[number]) > 1):
                return True
        
        return False
        


# Your TwoSum object will be instantiated and called as such:
# obj = TwoSum()
# obj.add(number)
# param_2 = obj.find(value)