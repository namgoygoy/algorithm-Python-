class Solution:
    def removeStars(self, s: str) -> str:
        result = []
        for i in range(len(s)):
            if s[i] == "*":
                result.pop()
            else:
                result.append(s[i])
                
        return "".join(result)