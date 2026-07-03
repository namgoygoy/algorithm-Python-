def solution(companyInfos, jobGroup, region, date):
    answer = 0
    
    for company in companyInfos:
        # 각 기업 정보 분해
        # company = [기업 이름, 직군 정보, 지역 정보, 채용 시작일, 채용 마감일]
        c_name, c_job, c_region, start_date, end_date = company
        
        # 1. 직군 조건 체크
        if c_job != jobGroup:
            continue
            
        # 2. 지역 조건 체크
        if c_region != region:
            continue
            
        # 3. 날짜 기간 체크 (시작일 <= 현재 날짜 <= 마감일)
        if start_date <= date <= end_date:
            answer += 1
            
    return answer

# 입출력 예제 1 테스트
companyInfos = [
    ["Company1", "Android", "Seoul", "2022-05-07T10:00:00", "2022-05-22T10:00:00"],
    ["Company2", "Android", "Seoul", "2022-05-10T10:00:00", "2022-05-24T10:00:00"],
    ["Company3", "Design", "Daegeon", "2022-05-05T10:00:00", "2022-05-19T10:00:00"]
]
jobGroup = "Android"
region = "Seoul"
date = "2022-05-08T10:00:00"

print(solution(companyInfos, jobGroup, region, date))  # 출력: 1