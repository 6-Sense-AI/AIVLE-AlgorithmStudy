# 이 바보야 진짜 아니야~

import sys

input = sys.stdin.readline

n = int(input())
lst = []

for _ in range(n):
    lst.append(int(input()))

dp = [0]*(n+1)

i = 0
max_v = 0
flag = 0

for i in range(1,n+1):
    if flag != 2:
        if max(dp[i-1]+lst[i-1],dp[i-2]+lst[i-1]) == dp[i-1]+lst[i-1]:
            dp[i] = dp[i-1]+lst[i-1]
            flag += 1
        else:
            dp[i] = dp[i-2]+lst[i-1]
            flag = 0
    else:
        flag = 0
        dp[i] = dp[i-1]
        continue

print(dp[-1])
