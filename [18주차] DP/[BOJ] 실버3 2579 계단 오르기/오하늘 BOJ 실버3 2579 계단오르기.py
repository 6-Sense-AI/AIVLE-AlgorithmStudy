import sys
input = sys.stdin.readline
# 너무 싫어해서 고른 계단 오르기 ~

# 조건 1. 한계단 or 두계단
# 2. 연속된 세개의 계단은 안됨 (시작점은 포함X)
# 3. 마지막 도착 계단은 반드시 밟아야 함

n = int(input())
arr = []
for i in range(n):
    arr.append(int(input().strip()))

dp = [0] * n # dp 생성

if n == 1: print(arr[0])
elif n == 2: print(arr[0]+arr[1])

else : # n>3
    dp[0] = arr[0] # 시작점
    dp[1] = arr[0]+arr[1] # 시작점 아님

    result = 0
    for i in range(2,n):
        # max (한계단의경우 = 현재값+이전값+dp[i-2] , 두계단의 경우 = 현재값 + dq[i-1])
        dp[i] = max(arr[i]+arr[i-1]+dp[i-3], arr[i]+dp[i-2])

    print(dp[n-1]) # 마지막 도착 계단