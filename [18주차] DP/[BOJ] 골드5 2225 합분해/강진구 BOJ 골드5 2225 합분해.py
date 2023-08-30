import sys

input = sys.stdin.readline

n, k = map(int, input().split())

# k-1개의 막대기가 n+1개의 위치에 몇개를 놓을 수 있는지 문제 중복허용
# n+k-1 중 k-1만큼 뽑기 중복없이

dp = [1 for _ in range(401)]

dp[1] = n+k-1

for i in range(2, n+k):
    dp[i] = int(dp[i-1]*(n+k-i)/i)

print(dp[k-1])