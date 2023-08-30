# 사자를 한 마리도 배치하지 않는 경우도 하나의 경우의 수로 친다
# 사자를 배치하는 경우의 수를 9901로 나눈 나머지를 출력

row = int(input())    # 세로의 길이
dp = [0] * 100000    # dp 리스트
dp[0], dp[1] = 3, 7

if row > 1:
    for i in range(2, row):
        dp[i] = (dp[i-1] * 2 + dp[i-2]) % 9901

print(dp[row-1])