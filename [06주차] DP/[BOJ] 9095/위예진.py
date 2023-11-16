import sys
input = sys.stdin.readline

n = int(input())    # 수의 개수 입력 받기
nums = [int(input()) for _ in range(n)]    # 수들 입력
dp = [0, 1, 2, 4]    # dp 초기화

for i in range(4, max(nums) + 1):
    dp.append(dp[i-1] + dp[i-2] + dp[i-3])
    
for number in nums:
    print(dp[number])