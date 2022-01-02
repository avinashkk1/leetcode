class Solution:
    def groupStrings(self, strings: List[str]) -> List[List[str]]:
        shiftedStrings = {}
        
        for index, string in enumerate(strings):
            s = str(len(string)) + '#'
            for i in range(1, len(string)):
                charDiff = ord(string[i]) - ord(string[i - 1])
                if charDiff < 0:
                    charDiff = 26 + charDiff
                s += str(charDiff) + '#'
            
            if s in shiftedStrings:
                shiftedStrings[s].append(index)
            else:
                shiftedStrings[s] = [index]
            
        ans = []
        for string, indices in shiftedStrings.items():
            groupStrings = []
            for index in indices:
                groupStrings.append(strings[index])
            ans.append(groupStrings)
        
        return ans
            
            
        