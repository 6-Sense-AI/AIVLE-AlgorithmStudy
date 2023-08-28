import sys
input = sys.stdin.readline
n = int(input()) # 돌 갯수
# 조건 1.상근이가 먼저 2. 홀수개로 가져갈 수 있음

if n%2 == 0: # 짝수면
    print('SK')
else: # 홀수면
    print('CY')