## 시간 복잡도 O(n^2)
# class Solution:
#     def findMaxAverage(self, nums: List[int], k: int) -> float:
#         if len(nums) == 1:
#             return nums[0] / k

#         max_total = 0
#         for i in range(len(nums) - k):
#             total = 0
#             for j in range(i, i + k):
#                 total += nums[j]
#             if total > max_total:
#                 max_total = total

#         return max_total / k


class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        current_sum = sum(nums[:k])
        max_sum = current_sum
        
        for i in range(k, len(nums)):
            current_sum = current_sum - nums[i - k] + nums[i]
            
            if current_sum > max_sum:
                max_sum = current_sum
                
        return max_sum / k