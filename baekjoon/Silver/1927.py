import heapq
import sys

input = sys.stdin.readline

heap = []

N = int(input())

for _ in range(N):
    x = int(input())

    if x > 0:
        # 최소 힙에 x를 추가
        heapq.heappush(heap, x)
        
    elif x == 0:
        if heap:
            # 힙이 비어있지 않다면, 가장 작은 값을 pop하여 출력
            # 최소값이 가장 위에 있게 되기 때문에 최소값이 반환됨
            # 마찬가지로 heappop 이후 힙 구조가 O(log N) 시간에 재정렬됩니다.
            print(heapq.heappop(heap))
        else:
            # 힙이 비어있다면 0을 출력
            print(0)