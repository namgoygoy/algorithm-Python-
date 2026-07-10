class Solution:
    def decodeString(self, s: str) -> str:
        countStack = []
        stringStack = []
        currentString = ""
        currentNum = 0
        
        for char in s:
            if char.isdigit():
                currentNum = currentNum * 10 + int(char)
            elif char == '[':
                countStack.append(currentNum)
                stringStack.append(currentString)
                currentString = ""
                currentNum = 0
            elif char == ']':
                repeatTimes = countStack.pop() 
                lastString = stringStack.pop()  
                
                currentString = lastString + (currentString * repeatTimes)
                
            else:
                currentString += char
                
        return currentString