# n의 최대값 = max( (n-1)열 대각선 dp, (n-2)열 최대값 dp ) + arr[n]

import sys
input = sys.stdin.readline

t = int(input())    # 테스트케이스의 수

for _ in range(t):
    n = int(input())    # 열의 수
    sticker = [list(map(int, input().split())) for _ in range(2)]    # 스티커 2차원 리스트
    dp = [[0] * (n + 1) for _ in range(2)]    # dp 2차원 리스트

    dp[0][1], dp[1][1] = sticker[0][0], sticker[1][0]
    if n > 1:
        dp[0][2], dp[1][2] = dp[1][1] + sticker[0][1], dp[0][1] + sticker[1][1]

    for i in range(3, n + 1):
        dp[0][i] = max(dp[1][i-1], max(dp[0][i-2], dp[1][i-2])) + sticker[0][i-1]
        dp[1][i] = max(dp[0][i-1], max(dp[0][i-2], dp[1][i-2])) + sticker[1][i-1]

    print(max(dp[0][n], dp[1][n]))