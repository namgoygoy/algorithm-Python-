import sys

# input = sys.stdin.readline  # 많은 입력을 받을 때는 sys.stdin.readline이 더 빠릅니다.

N = int(input())
cnt = 0

for _ in range(N):
    word = input()
    stack = []  # 1. 각 단어마다 스택을 새로 초기화합니다. (하나의 스택만 사용)

    for char in word:
        # 2. 스택 핵심 로직 수정
        if not stack:  # 스택이 비어있으면
            stack.append(char)
        else:
            if stack[-1] == char:  # 스택의 top과 현재 문자가 같으면
                stack.pop()        # 쌍을 이룸 (pop)
            else:
                stack.append(char) # 문자가 다르면 (새로운 쌍이 열림, push)

    # 3. 단어 처리가 끝난 후, 스택이 비어있는지 확인
    if not stack:
        cnt += 1

print(cnt)