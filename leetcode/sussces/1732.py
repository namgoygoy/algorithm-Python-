class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        max_height = 0
        height = 0
        for i in gain:
            height += i

            if max_height < height:
                max_height = height

        return max_height
        