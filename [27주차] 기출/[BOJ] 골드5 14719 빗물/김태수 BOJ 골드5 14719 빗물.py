# 답이 0인 예외를 제거 못함
# import sys
# input=sys.stdin.readline

# h,w = map(int,input().split())
# block = list(map(int,input().split()))

# cnt = 0
# for i in range(w-1):
#     if block[i] > block[i+1]:
#         max = block[i]
#         cnt += block[i]-block[i+1]
#     else:
#         max = block[i+1]
#         cnt += block[i+1]-block[i+1]
# print(cnt)

import sys
input=sys.stdin.readline

h,w = map(int,input().split())
block = list(map(int,input().split()))
cnt = 0

for i in range(1, w-1):
    left = max(block[ :i])
    right = max(block[i+1: ])
    m = min(left, right)
    if m>block[i]:
        cnt += m - block[i]

print(cnt)