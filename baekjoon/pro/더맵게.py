import heapq

def solution(scoville, K):
    # 1. scoville 리스트를 최소 힙으로 변환
    heapq.heapify(scoville)
    
    answer = 0
    
    # 2. 힙의 최소값(scoville[0])이 K보다 작은 동안 반복
    while scoville[0] < K:
        # 3. 힙의 원소가 2개 미만이면 K 이상으로 만들 수 없음
        if len(scoville) < 2:
            return -1
            
        # 4. 가장 맵지 않은 음식과 두 번째로 맵지 않은 음식을 꺼냄
        first = heapq.heappop(scoville)
        second = heapq.heappop(scoville)
        
        # 5. 두 음식을 섞어 새로운 스코빌 지수를 만듦
        new_scoville = first + (second * 2)
        
        # 6. 새로운 음식을 힙에 다시 추가
        heapq.heappush(scoville, new_scoville)
        
        # 7. 섞은 횟수 증가
        answer += 1
        
    return answer

# --- 예제 테스트 ---
scoville = [1, 2, 3, 9, 10, 12]
K = 7
print(solution(scoville, K))  # 출력: 2