class Solution:
    def reverseWords(self, s: str) -> str:
        li = s.strip().split(" ")
        result = []
        for i in range(len(li)):
            if li[i] != "":
                result.append(li[i])
        result_str = result[::-1]
        return " ".join(result_str)