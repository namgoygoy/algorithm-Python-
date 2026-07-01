def solution(TC, QWER):
    answer = []
    
    for tc in range(TC):
        grid = QWER[tc] # 현재 테스트 케이스의 16x16 격자 데이터
        version_str = ""
        
        # 상단 4개의 행을 순서대로 탐색 (i: 0, 1, 2, 3)
        for i in range(4):
            # 가로 4번부터 11번 인덱스까지가 버전 영역 (총 8칸)
            row_data = grid[i][4:12] 
            
            left_4 = row_data[0:4]  # 앞의 4칸
            right_4 = row_data[4:8] # 뒤의 4칸
            
            # 앞 4칸 XOR 연산 수행
            left_xor = left_4[0] ^ left_4[1] ^ left_4[2] ^ left_4[3]
            right_xor = right_4[0] ^ right_4[1] ^ right_4[2] ^ right_4[3]
            
            decimal_val = (left_xor * 2) + right_xor
            
            # 문자열로 이어 붙이기
            version_str += str(decimal_val)
            
        # "버전은 0으로 시작하지 않는다" 조건 만족을 위해 int로 변환 후 answer에 추가
        answer.append(int(version_str))
        
    return answer

