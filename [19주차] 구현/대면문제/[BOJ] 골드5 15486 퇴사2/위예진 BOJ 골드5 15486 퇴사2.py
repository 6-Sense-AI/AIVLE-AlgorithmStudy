# 뒤에서부터 계산
# max([현재꺼 + 현재꺼 했을 때의 끝난 날짜 dp], 바로 뒤의 dp )

import sys
input = sys.stdin.readline

n = int(input())    # 일수
meets = [list(map(int, input().split())) for _ in range(n)]    # [기간 t, 금액 p]

dp = [0] * n    # dp 리스트
# 시작(마지막) dp 초기화
if meets[n-1][0] > 1:     # 마지막 약속이 불가능하면, 0으로 초기화
    dp[n-1] = 0
else:    # 가능하면, 해당 금액
    dp[n-1] = meets[n-1][1]

# 뒤에서부터 순차적으로 dp 리스트 완성
for i, (t, p) in enumerate(meets[-2::-1]):
    day = n-i-2
    if day + (t - 1) < n:    # 해당 약속 가능하면, 비교
        if day + t == n:
            dp[day] = max(p, dp[day+1])
        else:
            dp[day] = max(p + dp[day+t], dp[day+1])
    else:     # 불가능하면, 바로 뒤의 dp 값
        dp[day] = dp[day+1]

print(dp[0])