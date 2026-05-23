import sys
# 가장 빨리 끝나는 강의실(최솟값)을 즉시 확인하기 위해
# 리스트 O(N) 대신, 우선순위 큐(힙) O(log N) 사용
import heapq

input = sys.stdin.readline

N = int(input())
lectures = []

for _ in range(N):
    lectures.append(list(map(int, input().split())))

# 강의 시작 시간 기준으로 정렬 (강의실 배정을 위해)
# 정렬이 안 되어 있어서, 오후 3시 수업을 먼저 처리했다고 칩시다. min_heap에 (17:00 종료)가 기록됩니다. (오후 5시에 방이 빔)
# 그 다음에 오전 9시 수업을 처리하려고 합니다. 비교식: if 17:00 <= 09:00: (거짓)
lectures.sort(key=lambda x: x[1])

min_heap = []
# 각 강의실에 배정된 강의 ID를 저장할 리스트
rooms = [0] * (N + 1)
cnt = 0

for id, start, end in lectures:
    # 가장 빨리 끝나는 강의실이 현재 강의 시작 시간 이전에 끝난다면 재사용  
    if min_heap and min_heap[0][0] <= start:
        _, room_id = heapq.heappop(min_heap)
        heapq.heappush(min_heap, (end, room_id))
        rooms[id] = room_id
    # 새로운 강의실이 필요한 경우    
    else:
        cnt += 1
        heapq.heappush(min_heap, (end, cnt))
        rooms[id] = cnt

print(cnt)
for i in range(1, N + 1):
    print(rooms[i])