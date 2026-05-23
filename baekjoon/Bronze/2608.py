N = int(input())
li = list(map(int, input().split()))
cnt = 0
sosu_cnt = 0


for i in range(N):
    for j in range(1, li[i]):
        if li[i] % j == 0:
            cnt += 1
    if cnt == 1:
        sosu_cnt += 1
    cnt = 0

print(sosu_cnt)    



