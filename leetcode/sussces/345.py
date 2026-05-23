class Solution:
    def reverseVowels(self, s: str) -> str:
        vowel = "aeiou"
        vowel_large = "AEIOU"
        vowel_li = []
        s_li = []
        for i in range(len(s)):
            s_li.append(s[i])
        for i in range(len(s)):
            if s[i] in vowel or s[i] in vowel_large:
                vowel_li.append(s[i])
        cnt = 1
        for j in range(len(s)):
            if s[j] in vowel or s[j] in vowel_large:
                s_li[j] = vowel_li[-cnt]
                cnt += 1
        s = "".join(s_li)
        return s

                
        