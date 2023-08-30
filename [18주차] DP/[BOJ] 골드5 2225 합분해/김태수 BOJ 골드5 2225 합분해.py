import sys
input = sys.stdin.readline

n, k = map(int,input().split())

dp = [[0] * 201 for _ in range(201)]

# k=1 이면 n에 상관없이 n이 되는 경우의 수는 1이다 (n 자신 1개)
for i in range(201):
    dp[1][i] = 1
    dp[2][i] = i+1

# 점화식 dp[i][j] = (dp[i][j-1] + dp[i-1][j])
for i in range(2, 201):
    dp[i][1] = i
    for j in range(2, 201):
        dp[i][j] = (dp[i][j-1] + dp[i-1][j]) % 1000000000

print(dp[k][n])