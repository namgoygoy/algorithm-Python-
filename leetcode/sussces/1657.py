from collections import Counter 

class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        if len(word1) != len(word2):
            return False

        for letter in word1:
            if letter not in word2:
                return False

        dict1 = Counter(word1).values()
        dict2 = Counter(word2).values()

        if sorted(dict1) == sorted(dict2):
            return True
        else:
            return False
        

## 더 좋은 방법
# from collections import Counter 

# class Solution:
#     def closeStrings(self, word1: str, word2: str) -> bool:
#         if len(word1) != len(word2):
#             return False

#         c1 = Counter(word1)
#         c2 = Counter(word2)

#         if set(c1.keys()) != set(c2.keys()):
#             return False

#         return sorted(c1.values()) == sorted(c2.values())