# 노가다로 규칙찾기
# dp[0]부터 해야한다.
# dp[0]을 두고 dp[1]부터 카운트하면 런타임 에러
import sys
input = sys.stdin.readline

n = int(input())
dp = [0] * (n+1)

dp[0] = 1
dp[1] = 3

for i in range(2, n+1):
    dp[i] = (2 * dp[i-1] + dp[i-2]) % 9901

print(dp[n])