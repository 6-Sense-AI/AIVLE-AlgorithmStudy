# 동물원
import sys
input = sys.stdin.readline

#가로로 두칸 세로로 n칸

n = int(input()) # 세로 칸

dp = [1] * n # 세로의 수에 따른 점화식 세우기

if n == 1 : print(3)
# elif n == 2 : print(7)
else :
    dp[0] = 3
    dp[1] = 7
    for i in range(2,n):
        dp[i] = (2*dp[i-1] + dp[i-2]) % 9901

    print(dp[n])