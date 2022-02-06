class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        startBraceStack = []
        stackIndexTrack = 0
        
        for i, ch in enumerate(s):
            if ch == '[':
                startBraceStack.append(stackIndexTrack)
                
            if ch == ']':
                lastStartBraceIndex = startBraceStack[-1]
                
                tempString = ''.join(stack[lastStartBraceIndex + 1 :])
                
                numOfTimesToRepeat = ''
                for j in range(lastStartBraceIndex - 1, -1, -1):
                    if stack[j].isdigit():
                        numOfTimesToRepeat = str(stack[j]) + numOfTimesToRepeat
                    else:
                        break
                
                #print(numOfTimesToRepeat)
                numOfDigits = len(numOfTimesToRepeat)
                numOfTimesToRepeat = int(numOfTimesToRepeat)

                
                
                tempString *= numOfTimesToRepeat
                
                stackIndexToDelete = -1 * (len(stack) - lastStartBraceIndex + numOfDigits)
                stack = stack[:stackIndexToDelete]
                stack.append(tempString)
                startBraceStack.pop()
                stackIndexTrack += stackIndexToDelete + 1
                
            else:
                stack.append(ch)
                stackIndexTrack += 1
                
        
        return ''.join(stack)
        