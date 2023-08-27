import sys

input = sys.stdin.readline

t = int(input())

for _ in range(t):
    n = int(input())

    dp = []

    for _ in range(2):
        dp.append(list(map(int, input().split())))
# n = 1보다 커야 런타임 에러 안남
    if n>1:
        dp[0][1] += dp[1][0]
        dp[1][1] += dp[0][0]
# 앞에 두개씩 비교하면서 기록(메모이제이션) 하면서 진행 바텀업 형식 어차피 3개 묶음 중에서 최대값을 구하면 계속 최대값으로 진행가능
    for i in range(2,n):
        dp[0][i] += max(dp[1][i-1], dp[1][i-2])
        dp[1][i] += max(dp[0][i-1], dp[0][i-2])
    
    print(max(dp[0][-1], dp[1][-1]))
        