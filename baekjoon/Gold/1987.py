import sys

input = sys.stdin.readline

# setrecursionlimit(10**6) -> GB단위로 들어 감

R, C = map(int, input().split())
# 보드 입력
board = [list(input().strip()) for _ in range(R)]

# 상하좌우 이동 방향
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# 방문 기록을 위한 집합
# 리스트 대신 set을 쓰는 이유:set 안에 있는지 확인하는 속도(in 연산)이 리스트보다 훨씬 빠름
visited_alphabets = set()
max_count = 1

def dfs(x, y, count):
    global max_count
    max_count = max(max_count, count)

    # 네 방향으로 이동
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        # 보드 범위 내에 있고, 방문하지 않은 알파벳인 경우
        if 0 <= nx < R and 0 <= ny < C:
            if board[nx][ny] not in visited_alphabets:

                # 방문 처리 및 재귀 호출    
                visited_alphabets.add(board[nx][ny])
                dfs(nx, ny, count + 1)

                # 백트래킹: 방문 처리 해제
                visited_alphabets.remove(board[nx][ny])
                
                # 최대 20×20=400 가지
                # 2^26=67,108,864 (약 6천 7백만) 가지

visited_alphabets.add(board[0][0])
dfs(0, 0, 1)
print(max_count)