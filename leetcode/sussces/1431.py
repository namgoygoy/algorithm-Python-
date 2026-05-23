class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        candy_list = []
        for i in range(len(candies)):
            if candies[i] + extraCandies >= max(candies):
                candy_list.append(True)
            else:
                candy_list.append(False)
        return candy_list
