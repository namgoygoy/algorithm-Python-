import heapq

def solution(operations):
    min_heap = []
    max_heap = []
    
    # 각 숫자의 유효한(삭제되지 않은) 개수를 추적
    count = {} 

    for operation in operations:
        op, num_str = operation.split()
        num = int(num_str)
        
        if op == 'I':
            # 1. 삽입
            heapq.heappush(min_heap, num)
            heapq.heappush(max_heap, -num)
            count[num] = count.get(num, 0) + 1
            
        elif op == 'D':
            if num == -1:
                # 2-1. 최솟값 삭제
                # min_heap을 청소 (유효하지 않은 값들 제거)
                # count가 0이라는 것은 max_heap에서 이미 삭제된 값이라는 의미
                while min_heap and count.get(min_heap[0], 0) == 0:
                    heapq.heappop(min_heap)
                
                if min_heap:
                    # 유효한 최솟값 삭제
                    min_val = heapq.heappop(min_heap)
                    count[min_val] -= 1
                    
            elif num == 1:
                # 2-2. 최댓값 삭제
                # max_heap을 청소 (유효하지 않은 값들 제거)
                # count가 0이라는 것은 min_heap에서 이미 삭제된 값이라는 의미
                while max_heap and count.get(-max_heap[0], 0) == 0:
                    heapq.heappop(max_heap)
                    
                if max_heap:
                    # 유효한 최댓값 삭제
                    max_val = -heapq.heappop(max_heap)
                    count[max_val] -= 1

    # 3. 모든 연산 후, 유효한(count > 0) 값들만 남도록 힙을 최종 정리
    while min_heap and count.get(min_heap[0], 0) == 0:
        heapq.heappop(min_heap)
    while max_heap and count.get(-max_heap[0], 0) == 0:
        heapq.heappop(max_heap)

    # 4. 결과 반환
    if not min_heap: # (또는 max_heap)
        return [0, 0]
    else:
        return [-max_heap[0], min_heap[0]]

# --- 예제 테스트 ---
op1 = ["I 16", "I -5643", "D -1", "D 1", "D 1", "I 123", "D -1"]
op2 = ["I -45", "I 653", "D 1", "I -642", "I 45", "I 97", "D 1", "D -1", "I 333"]

print(f"결과 1: {solution(op1)}")  # 출력: [0, 0]
print(f"결과 2: {solution(op2)}")  # 출력: [333, -45]