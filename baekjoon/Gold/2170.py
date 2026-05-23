import sys
input = sys.stdin.readline

N = int(input())
lines = []

for _ in range(N):
    x, y = map(int, input().split())
    lines.append((x, y))

# NlogN 
# 예: [ (5, 8), (1, 4), (3, 6) ] 이런 순서면 겹치는 구간을 제대로 계산 못함 
# 실제로는 선 (1,4)가 (5,8) 앞쪽이라 겹치지 않음에도 next_start <= current_end으로 작동
lines.sort()

length = 0

# 초기값 잡기 
# 안 잡으면 current_start/current_end가 존재하지 않아 에러 발생
current_start = lines[0][0]
current_end = lines[0][1]

for i in range(len(lines)):
    next_start, next_end = lines[i]
    # 현재 병합 중인 구간과 겹치는가?
    if next_start <= current_end:
        current_end = max(next_end, current_end)
    else:
        # 지금까지 병합된 구간의 길이를 최종 합계 
        length += current_end - current_start

        # 새 구간을 갱신
        current_start = next_start
        current_end = next_end

length += current_end - current_start

print(length)

