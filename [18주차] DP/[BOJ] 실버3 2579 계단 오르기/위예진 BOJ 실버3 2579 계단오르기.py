# 도착지점에서부터 경우의 수 생각!

import sys
input = sys.stdin.readline

n = int(input())    # 계단 높이
steps = [int(input()) for _ in range(n)]    # 각 계단의 점수 리스트
dp = [0] * (n + 1)    # 현재 계단까지의 최대 점수
dp[1] = steps[0]
if n > 1:
    dp[2]=dp[1]+steps[1]
for i in range(3,n+1):
    dp[i] = steps[i-1] + max(dp[i-3] + steps[i-2], dp[i-2])

print(dp[n])    # 최종 계단에 도착했을 때의 최대값