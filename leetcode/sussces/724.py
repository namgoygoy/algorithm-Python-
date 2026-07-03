class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        for pivot in range(len(nums)):
            # nums[index]과 달리 nums[pivot + 1:]와 같은 파이썬 슬라이싱은 에러가 발생하지 않는다고 함.
            # 범위를 벗어나도 빈 리스트 []를 제공하며, sum함수도 빈 리스트에 경우 0을 반환
            if sum(nums[:pivot]) == sum(nums[pivot + 1:]):
                return pivot
        return -1