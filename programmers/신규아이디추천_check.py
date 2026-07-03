def solution(new_id):
    filter_letter = "qwertyuiopasdfghjklzxcvbnm1234567890-_."
    upper_letter = "QWERTYUIOPASDFGHJKLZXCVBNM"
    
    # 1~2단계 통합 처리
    result = ""
    for letter in new_id:
        if letter in upper_letter:
            result += letter.lower()
        elif letter in filter_letter:  
            result += letter

    # 3단계: 마침표 연속 처리 
    while ".." in result:
        result = result.replace("..", ".")
    
    # 4단계: 처음과 끝 마침표 제거
    if result and result[0] == ".":
        result = result[1:]  # 0번을 지우는 대신, 1번 인덱스부터 끝까지 잘라서 새 문자열 생성
    if result and result[-1] == ".":
        result = result[:-1] # 마지막 글자를 제외하고 잘라서 새 문자열 생성
    
    # 5단계: 빈 문자열 처리
    if result == "":
        result = "a"
    
    # 6단계: 16자 이상인 경우 자르기
    if len(result) >= 16:
        temp = result[:15]  # 반복문 대신 슬라이싱으로 0부터 14번째 글자(총 15자)까지 한 방에 자르기
    else:
        temp = result       # 16자 미만이면 그대로 넘겨주기
        
    # 잘라낸 후 끝에 마침표가 남았는지 다시 체크
    if temp and temp[-1] == ".":
        temp = temp[:-1]
    
    # 7단계: 길이가 2자 이하인 경우 늘리기
    if len(temp) <= 2:
        while len(temp) < 3:
            temp += temp[-1]  # 맨 마지막 글자 이어 붙이기
            
    new_id = temp
    return new_id

