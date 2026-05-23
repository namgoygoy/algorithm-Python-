answer = []

for _ in range(10):
    N = int(input())
    answer.append(N % 42)

unique_answer = set(answer)

print(len(unique_answer))