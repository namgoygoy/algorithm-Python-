n = int(input())

col_used = [False] * n

# 최대값: (3, 3)에서 3 + 3 = 6
# 변경된 최대값: (n-1) + (n-1) = 2n - 2
# 만약 0, 1, 2, 3까지 4개의 숫자를 배열에 저장하고 싶다고 가정해 봅시다.
# 가장 큰 숫자는 3입니다.
# 하지만 필요한 배열의 크기는 4입니다. ( arr[0], arr[1], arr[2], arr[3] )
# 즉, 필요한 크기 = (가장 큰 인덱스) + 1 이 됩니다.
diag1_used = [False] * (2 * n - 1)
diag2_used = [False] * (2 * n - 1)

count = 0 

# 로----우 컬||||럼
def backtrack(row):
    global count, n
    # 성공적으로 n퀸을 배치한 경우
    if row == n:
        count += 1
        return
    
    for col in range(n):
        # 해당 열과 대각선이 이미 사용된 경우 건너뜀, backtrack(row)
        if col_used[col]:
            continue
        # (0, 3), (1, 2), (2, 1), (3, 0) 이 3번 대각 row + col 값이 3 규칙성
        if diag1_used[row + col]:
            continue
        if diag2_used[row - col + n - 1]:   
            continue
        
        # 해당 열과 대각선을 사용 표시
        col_used[col] = True
        diag1_used[row + col] = True
        diag2_used[row - col + n - 1] = True
        # 다음 행으로 이동
        backtrack(row + 1)
        # 사용 표시 해제 (백트래킹)
        col_used[col] = False
        diag1_used[row + col] = False
        diag2_used[row - col + n - 1] = False

backtrack(0)    

print(count)