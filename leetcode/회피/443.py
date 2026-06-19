class Solution:
    def compress(self, chars: List[str]) -> int:
        write = 0  # 압축된 결과를 적을 포인터
        read = 0   # 원본 배열을 읽어나갈 포인터
        
        while read < len(chars):
            start = read  # 현재 문자 그룹의 시작점 기억
            
            # 1. 같은 글자가 연속되는 동안 read 포인터를 전진시킵니다.
            while read < len(chars) and chars[read] == chars[start]:
                read += 1
            
            # 2. 그룹의 첫 번째 글자를 write 자리에 적습니다.
            chars[write] = chars[start]
            write += 1
            
            # 3. 글자의 개수를 계산합니다 (현재 read 위치 - 시작 위치)
            count = read - start
            
            # 4. 개수가 2개 이상일 때만 숫자를 문자로 바꿔서 채워 넣습니다.
            if count > 1:
                for digit in str(count):
                    chars[write] = digit
                    write += 1
                    
        # 최종적으로 write 포인터의 위치가 새로운 배열의 길이가 됩니다.
        return write