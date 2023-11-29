import sys
input = sys.stdin.readline

n = int(input())
arr = [list(map(int, input().split())) for _ in range (n)]

dp = [[0] * n for _ in range(n)] # 2차원 dp 최소

print(dp)

for i in range(len(arr[0])):
    dp[0][i] = arr[0][i] # dp 첫줄

dp2 = dp.copy() # 최대

# dp[y][x] 형태임
for j in range(1,n): # 세로 y 
    for i in range(0,n): # 가로 x
        if i < 0 : # 왼쪽이 없는 경우
            dp[i][j] = arr[i][j] + min(dp[i-1][j],dp[i-1][j+1])
            dp2[i][j] = arr[i][j] + max(dp2[i-1][j],dp2[i-1][j+1])
        elif i > n : # 오른쪽이 없는 경우
            dp[i][j] = arr[i][j] + min(dp[i-1][j],dp[i-1][j-1])
            dp2[i][j] = arr[i][j] + max(dp2[i-1][j],dp2[i-1][j-1])
        else: # 둘다 가능
            dp[i][j] = arr[i][j] + min(dp[i-1][j],dp[i-1][j-1],dp[i-1][j+1])
            dp2[i][j] = arr[i][j] + max(dp2[i-1][j],dp2[i-1][j-1],dp2[i-1][j+1])

print(max(dp2[n]),min(dp[n]))