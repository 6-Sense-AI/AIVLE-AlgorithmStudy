import sys, copy
from collections import deque


input = sys.stdin.readline

n = int(input())

seq = list(map(int, input().split()))

opr = dict()

opr['+'], opr['-'], opr['*'], opr['/'] = map(int, input().split())

# 앞에서부터 순서대로 제일 큰값, 제일 작은값 찾기
# 빼기랑 나누기를 최대한 뒤로 나누기가 빼기보단 먼저 그리고 가장 마지막에 곱하기 있다면 -가 될때가 최소
opr_copy = copy.deepcopy(opr)

# # 최대 구하기
# que = deque(seq)
# x = que.popleft()
# while que:
#     y = que.popleft()
#     if opr['-'] != 0:
#         x -= y
#         opr['-'] -= 1
#     elif opr['/'] != 0:
#         if x >= 0 :
#             x //= y
#         else:
#             x = -1*(-1*x//y)
#         opr['/'] -= 1
#     elif opr['+'] != 0:
#         x += y
#         opr['+'] -= 1
#     else:
#         if opr['*'] != 0:
#             x *= y
#             opr['*'] -= 1
# print(x)

# # 최소 구하기
# que = deque(seq)

# x = que.popleft()
# while que:
#     y = que.popleft()
#     if opr_copy['-'] != 0:
#         if opr_copy['+'] != 0:
#             x += y
#             opr_copy['+'] -= 1
#         elif opr_copy['/'] != 0:
#             if x >= 0 :
#                 x //= y
#             else:
#                 x = -1*((-1*x)//y)
#             opr_copy['/'] -= 1
#         elif opr_copy['-'] != 0:
#             x -= y
#             opr_copy['-'] -= 1
#         else:
#             if opr_copy['*'] != 0:
#                 x *= y
#                 opr_copy['*'] -= 1
#     else:
#         if opr_copy['*'] != 0:
#             x *= y
#             opr_copy['*'] -= 1
#         elif opr_copy['+'] != 0:
#             if opr_copy['+'] != 0:
#                 x += y
#                 opr_copy['+'] -= 1
#         else:
#             if x >= 0 :
#                 x //= y
#             else:
#                 x = -1*((-1*x)//y)
#             opr_copy['/'] -= 1
# print(x)

max_value = -1e9
min_value = 1e9
def dfs(i, arr):
    global min_value, max_value
    if i == n:
        max_value = max(max_value, arr)
        min_value = min(min_value, arr)
    else:
        if opr['+'] > 0:
            opr['+'] -= 1
            dfs(i+1, arr+seq[i])
            opr['+'] += 1
        if opr['-'] > 0:
            opr['-'] -= 1
            dfs(i+1, arr-seq[i])
            opr['-'] += 1
        if opr['*'] > 0:
            opr['*'] -= 1
            dfs(i+1, arr*seq[i])
            opr['*'] += 1
        if opr['/'] > 0:
            opr['/'] -= 1
            dfs(i+1, int(arr/seq[i]))
            opr['/'] += 1

dfs(1, seq[0])

print(max_value)
print(min_value)