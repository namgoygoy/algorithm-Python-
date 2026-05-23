expression = input()
# 스택을 이용한 중위 표기법 -> 후위 표기법 변환
# 연산자의 우선순위와 괄호 처리를 위해 스택이 적합
stack = []
answer = ''

for ch in expression:
    if ch == '(':
        stack.append(ch)
    elif ch == ')':
        # '(' 가 나올 때까지 스택에서 pop
        while stack and stack[-1] != '(':
            answer += stack.pop()
        stack.pop()
    # 우선순위가 높은 연산자 처리
    elif ch == '*' or ch == '/':
        while stack and (stack[-1] == '*' or stack[-1] == '/'):
            answer += stack.pop()
        # 해당 연산자 스택에 추가    
        stack.append(ch)
    # 우선순위가 낮은 연산자 처리
    elif ch == '+' or ch == '-':
        # (를 제외한 어떤 연산자(*, /, +, -)가 있더라도, 그 연산자들이 항상 먼저 계산되어야 합니다. 
        # 따라서 (를 만나기 전까지 스택의 모든 연산자를 answer로 pop 
        while stack and stack[-1] != '(':
            answer += stack.pop()
        stack.append(ch)
    # 피연산자 처리
    else:
        answer += ch

# 스택에 남아있는 연산자들 처리
while stack:
    answer += stack.pop()

print(answer) 