class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        cnt_dict = {}
        for num in arr:
            if num in cnt_dict:
                cnt_dict[num] += 1
            else:
                cnt_dict[num] = 1

        # [cnt_dict.values()] != list(cnt_dict.values()) 라고 함.
        # ([3, 2, 1]) != [3, 2, 1] 이렇게 다름
        cnt_list = list(cnt_dict.values())
        cnt_set = set(cnt_list)

        if len(cnt_list) == len(cnt_set):
            return True
        else:
            return False


