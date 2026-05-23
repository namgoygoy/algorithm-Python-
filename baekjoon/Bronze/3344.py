N = int(input())

start-point = [0][0]
arrrys = [[0 for _ in range(N)] for _ in range(N)]

for i in range(N):
    for j in range(N):
        up = arrrys[i][j] 
        left = arrrys[i][j-1] if j-1 >= 0 else 0
        down = arrrys[i-1][j] if i-1 >= 0 else 0
        right = arrrys[i-1][j-1] if i-1 >= 0 and j-1 >= 0 else 0
        