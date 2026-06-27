class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        cnt = 0
        for i in range(len(flowerbed)):
            if flowerbed[i] == 0:
                left_emtpy = (i == 0) or (flowerbed[i-1] == 0)
                right_emtpy = (i == len(flowerbed) - 1) or (flowerbed[i+1] == 0)
            
                if left_emtpy and right_emtpy:
                    flowerbed[i] = 1
                    cnt += 1

        if cnt >= n:
            return True
        else:
            return False
