import sys
input = sys.stdin.readline

n = int(input())    # 정수 삼각형의 크기
tri = [list(map(int, input().split())) for _ in range(n)]    # 정수 삼각형의 정보
dp = [[0] * i for i in range(1, n + 1)]    # 해당 위치의 최대 합
dp[0] = tri[0]    # 시작 위치 초기화
    
# 순차적으로 탐색
for d in range(1, n):    # (2 ~ n) 탐색
    for i in range(d + 1):
        if i == 0:    # 왼쪽 변의 값이라면,
            dp[d][i] = tri[d][i] + dp[d - 1][i]    # 바로 위의 값
        elif i == d:    # 오른쪽 변의 값이라면,
            dp[d][i] = tri[d][i] + dp[d - 1][i - 1]    # 바로 위의 값
        else:     # 중앙의 값이라면,
            dp[d][i] = tri[d][i] + max(dp[d - 1][i - 1:i + 1])    # (d - 1)의 (i - 1, i) 탐색
            
print(max(dp[n - 1]))