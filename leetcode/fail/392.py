class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if len(s) > len(t):
            return False
        
        pointer = 0
        cnt = 0
        for i in range(len(s)):
            for j in range(pointer, len(t)):
                if s[i] == t[j]:
                    if (j == 0 and pointer ==0) or pointer < j:
                        cnt += 1
                        pointer = j 
                        break

        if cnt >= len(s):
            return True
        else:
            return False 

