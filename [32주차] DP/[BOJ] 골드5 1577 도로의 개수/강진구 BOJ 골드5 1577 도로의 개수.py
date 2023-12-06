# 중복은 해결 못했습니다.
import sys, numpy

input = sys.stdin.readline

n,m = map(int, input().split())

k = int(input())

road = []

dp = [[0]*(m+1) for _ in range(n+1)]
for _ in range(k):
    a,b,c,d = map(int, input().split())
    # 위에서 내려오는거 -1 옆에서 오는거 -2 둘다 -3
    if a>c:
        dp[a][b] += -1
    elif b>d:
        dp[a][b] += -2
    elif c>a:
        dp[c][d] += -1
    else:
        dp[c][d] += -2
    
print(numpy.array(dp))

# 방법 수 구하기
for i in range(n+1):
    for j in range(m+1):
        if i == 0 and j == 0:
            continue
        else: # 둘다 걸리는 경우도 생각해줘야 함
            if i==0 or j==0:
                if dp[i][j] == 0:
                    if i>1 and dp[i-1][j] == 0:
                        dp[i][j] = 0
                    elif j>1 and dp[i][j-1] == 0:
                        dp[i][j] = 0
                    else:
                        dp[i][j] = 1
                else:
                    if dp[i][j] == -1:
                        if j != 0:
                            dp[i][j] = dp[i][j-1]
                        else:
                            dp[i][j] = 0
                    elif dp[i][j] == -2:
                        if i != 0:
                            dp[i][j] = dp[i-1][j]
                        else:
                            dp[i][j] = 0
                    elif dp[i][j] == -3:
                        dp[i][j] = 0
            else:
                if dp[i][j] == -1:
                    if j != 0:
                        dp[i][j] = dp[i][j-1]
                    else:
                        dp[i][j] = 0
                elif dp[i][j] == -2:
                    if i != 0:
                        dp[i][j] = dp[i-1][j]
                    else:
                        dp[i][j] = 0
                elif dp[i][j] == -3:
                    dp[i][j] = 0
                else:
                    dp[i][j] = dp[i][j-1]+dp[i-1][j]

print(dp[-1][-1])
print(numpy.array(dp))