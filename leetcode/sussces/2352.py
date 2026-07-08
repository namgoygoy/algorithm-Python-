class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        cnt = 0
        for row in grid:
            for i in range(len(grid)):
                li = []
                for j in range(len(grid)):
                    li.append(grid[j][i])
                    if row == li:
                        cnt += 1
        return cnt
        
## 해시 맵으로 푸는 방식 
# from collections import Counter
# from typing import List

# class Solution:
#     def equalPairs(self, grid: List[List[int]]) -> int:
#         n = len(grid)
#         row_counts = Counter(tuple(row) for row in grid)
        
#         cnt = 0
#         for c in range(n):
#             col = tuple(grid[r][c] for r in range(n))
#             if col in row_counts:
#                 cnt += row_counts[col]
                
#         return cnt