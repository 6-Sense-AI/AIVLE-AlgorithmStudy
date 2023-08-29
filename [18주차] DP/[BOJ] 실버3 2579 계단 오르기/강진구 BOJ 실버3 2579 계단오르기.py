import sys

input = sys.stdin.readline

n = int(input())

stairs = [0]*(301)

for i in range(1,n+1):
    stairs[i] = int(input())

# 이렇게 초기화 안해주면 런타임 오류남 왜 그럴까요?
dp = [0]*(301)

# 바텀업 방식(앞에 두개를 비교해서 내가 있는칸을 최대로 최신화)
dp[1] = stairs[1]
dp[2] = stairs[1]+stairs[2]
dp[3] = max(stairs[1]+stairs[3], stairs[2]+stairs[3])

for i in range(4,n+1):
    dp[i] = max(dp[i-2]+stairs[i], dp[i-3]+stairs[i-1]+stairs[i])

print(dp[n])