N = int(input())
li = list(map(int, input().split()))
answer = []
total_score = 0

for i in range(N):
    answer.append(li[i] / max(li) * 100)

for j in range(N):
    total_score += answer[j]

print(total_score / N)

    
