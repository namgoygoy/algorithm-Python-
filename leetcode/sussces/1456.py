class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        check = "aeiou"
        max_temp = 0
        for i in range(k):
            if s[i] in check:
                max_temp += 1
                
        temp = max_temp

        for j in range(k, len(s)):
            if s[j-k] in check:
                temp -= 1
            if s[j] in check:
                temp += 1
            if temp > max_temp:
                max_temp = temp


        return max_temp