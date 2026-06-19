class Solution:
    def maxArea(self, height: List[int]) -> int:
        most_water = 0
        left = 0
        right = len(height) - 1 
        while left < right:
            width = right - left
            current_water = width * min(height[left], height[right])

            if most_water < current_water:
                most_water = current_water
            
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        return most_water

