class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        right = len(nums) - 1
        left = 0
        cnt = 0
        nums.sort()
        while left < right:
            if nums[left] + nums[right] > k:
                right -= 1
            elif nums[left] + nums[right] < k:
                left += 1
            else:
                cnt += 1
                right -= 1
                left += 1
        return cnt


