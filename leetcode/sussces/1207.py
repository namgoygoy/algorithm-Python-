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


## 이렇게도 풀 수 있음
# from collections import Counter

# class Solution:
#     def uniqueOccurrences(self, arr: List[int]) -> bool:
#         # 1. Counter를 이용해 빈도수 계산 객체 생성
#         # Counter(arr) 결과 예시: Counter({1: 3, 2: 2, 3: 1})
#         counts = Counter(arr).values()
        
#         # 2. 빈도수 묶음의 길이와 set(중복제거)의 길이를 한 줄로 비교하여 반환
#         return len(counts) == len(set(counts))