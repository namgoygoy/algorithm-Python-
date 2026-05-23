# 인풋 3개 받기
# 받아서 곱하기 
# 곱한거 스트링타입으로 바꿔서 갯수 변수에 더하기

N = int(input())
M = int(input())
K = int(input())
total = str(N * M * K)
count_li = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

for i in range(len(total)):
    if total[i] == '0':
        count_li[0] += 1
    elif total[i] == '1':
        count_li[1] += 1
    elif total[i] == '2':
        count_li[2] += 1
    elif total[i] == '3':
        count_li[3] += 1
    elif total[i] == '4':
        count_li[4] += 1
    elif total[i] == '5':
        count_li[5] += 1
    elif total[i] == '6':
        count_li[6] += 1
    elif total[i] == '7':
        count_li[7] += 1
    elif total[i] == '8':
        count_li[8] += 1
    elif total[i] == '9':
        count_li[9] += 1

for j in range(len(count_li)):
    print(count_li[j])


