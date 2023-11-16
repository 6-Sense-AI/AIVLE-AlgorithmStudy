import sys
input = sys.stdin.readline

k = int(input())

for _ in range(k):
    dp = [0]*11
    n = int(input())

    dp[1]=1 # n=1 일때 1
    dp[2]=2 # n=2 일때 2
    dp[3]=4 # n=3 일때 4

    for i in range(4, n+1):
        dp[i] = dp[i-3] + dp[i-2] + dp[i-1]

    print(dp[n])
