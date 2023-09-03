# 0부터 N까지의 정수 K개를 더해서 그 합이 N이 되는 경우의 수
n, k = map(int, input().split())

# dp 리스트: (k X n)
dp = [[0] * (n + 1) for _ in range(k + 1)]
# k=1이면, n에 상관없이 경우의 수 -> 1개
dp[1] = [1] * (n + 1)
# n=1이면, 경우의 수 -> k개20
for i in range(1,k+1):
    dp[i][1] = i

# dp 리스트 완성: 현재 = (상+좌)
for r in range(2, k + 1):
    for c in range(2, n + 1):
        dp[r][c] = (dp[r-1][c] + dp[r][c-1]) % 1000000000    # 답을 1,000,000,000으로 나눈 나머지를 출력

print(dp[k][n])