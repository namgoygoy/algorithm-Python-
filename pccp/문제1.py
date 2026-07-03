def solution(cardGroup):
    # 1. 문양 우선순위 딕셔너리 (낮은 숫자가 높은 우선순위)
    suit_priority = {'C': 0, 'D': 1, 'H': 2, 'S': 3}
    
    # 2. 숫자/글자 우선순위 딕셔너리
    ranks = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
    rank_priority = {rank: i for i, rank in enumerate(ranks)}
    
    def get_sort_key(card):
        # card[0]은 숫자/글자 또는 "JK", card[1]은 문양
        rank_or_joker, suit = card[0], card[1]
        
        if rank_or_joker == "JK":
            # 조커 카드 규칙:
            # (1, 문양 가중치, 0) -> 조커 여부가 1이므로 일반 카드(0)보다 항상 뒤로 감
            return (1, suit_priority[suit], 0)
        else:
            # 일반 카드 규칙:
            # (0, 문양 가중치, 숫자 가중치)
            return (0, suit_priority[suit], rank_priority[rank_or_joker])
            
    # 정렬 후 결과 반환
    return sorted(cardGroup, key=get_sort_key)

# 입출력 예제 1 테스트
ex_input = [["JK", "H"], ["K", "C"], ["J", "D"], ["JK", "C"]]
print(solution(ex_input))
# 출력 결과: [['K', 'C'], ['J', 'D'], ['JK', 'C'], ['JK', 'H']]