import sys
input = sys.stdin.readline

# 입력받기
n, m = map(int, input().split())
# q = list(map(int, input().split()))
# k = list(map(int,input().split()))
# p = list(map(int, input().split()))

chess = [[False] * m for _ in range(n)]

# 체스판에 말 집어넣기
for i in ['Q', 'K', 'P']:
    tmp = list(map(int, input().split()))
    for j in range(1, tmp[0] * 2 + 1, 2):
        chess[tmp[j]-1][tmp[j+1]-1] = i

# Queen, Knight 범위
q_dx = [-1, 1, 0, 0, -1, -1, 1, 1]
q_dy = [0, 0, -1, 1, -1, 1, -1, 1]
k_dx = [-2, -2, -1, -1, 2, 2, 1, 1]
k_dy = [-1, 1, -2, 2, -1, 1, -2, 2]