import sys
input = sys.stdin.readline

# 입력받기
n = int(input())

# 규칙만 찾으면 금방
if n % 2 == 0:
    print('SK')
else:
    print('CY')