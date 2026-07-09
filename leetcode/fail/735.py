class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        
        for ast in asteroids:
            # 충돌이 일어나는 조건: 스택에 소행성이 있고, 스택 탑이 오른쪽(+)이고, 현재 소행성이 왼쪽(-)일 때
            while stack and stack[-1] > 0 and ast < 0:
                # 1. 현재 소행성이 더 커서 스택 탑을 파괴하는 경우
                if stack[-1] < abs(ast):
                    stack.pop()
                    continue # 다음 스택 탑과 다시 비교하기 위해 while문 계속 진행
                
                # 2. 두 소행성의 크기가 같아서 둘 다 파괴되는 경우
                elif stack[-1] == abs(ast):
                    stack.pop()
                
                # 3. 스택 탑이 더 커서 현재 소행성이 파괴되는 경우 (위의 두 조건이 모두 아닐 때)
                # 여기 걸리면 loop를 탈출하며, 아래의 else 블록도 실행되지 않아 ast는 스택에 추가되지 않음
                break
                
            else:
                # while문이 break 없이 무사히 끝났다 = 현재 소행성이 살아남았다!
                # (충돌 상황이 없었거나, 왼쪽 소행성이 스택 탑의 모든 오른쪽 소행성을 파괴했을 때)
                stack.append(ast)
                
        return stack