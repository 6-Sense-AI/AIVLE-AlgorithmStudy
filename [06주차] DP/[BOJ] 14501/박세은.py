import sys

input = sys.stdin.readline

n = int(input())
lst = []

for _ in range(n):
    t, p = map(int, input().split())
    lst.append((t, p))

dp = [0] * (n+1)

for i in range(1, n+1):
    dp[i] = lst[i-1][1]
    x = i + lst[i-1][0]
    while x <= 7:
        dp[i] += lst[x-1][1]
        x += lst[x-1][0]
        
print(min(dp))
