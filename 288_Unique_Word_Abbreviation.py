class ValidWordAbbr:

    def __init__(self, dictionary: List[str]):
        self.dictionary = defaultdict(set)
        for string in dictionary:
            if len(string) <= 2:
                self.dictionary[string].add(string)
            else:
                temp = string[0] + str(len(string) - 2) + string[-1]
                self.dictionary[temp].add(string)
                
            
                
        

    def isUnique(self, word: str) -> bool:
        if len(word) <= 2:
            abbr = word
        else:
            abbr = word[0] + str(len(word) - 2) + word[-1]
        
        if abbr not in self.dictionary:
            return True
        if self.dictionary[abbr] == set([word]):
            return True
        return False
        


# Your ValidWordAbbr object will be instantiated and called as such:
# obj = ValidWordAbbr(dictionary)
# param_1 = obj.isUnique(word)