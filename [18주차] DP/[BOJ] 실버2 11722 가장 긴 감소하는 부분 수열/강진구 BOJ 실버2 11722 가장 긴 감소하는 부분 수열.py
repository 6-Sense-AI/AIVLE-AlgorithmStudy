import sys

input = sys.stdin.readline

n = int(input())

seq = list(map(int, input().split()))

dp = [1]*n

# 앞에 더 큰애가 있다면 해당 인덱스로 이동
for idx in range(n):
    for i in range(idx):
        if seq[idx]<seq[i] and dp[i]+1>dp[idx]:
            dp[idx] = dp[i]+1
        
print((dp))
# 처음엔 while문을 거꾸로 돌았는데 그럴 필요가 없다!