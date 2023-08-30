# 시간초과 뜸

n = int(input())
plan = [list(map(int, input().split())) for _ in range(n)]
dp = [0] * n  # 시작지점별 최댓값

for i in range(n):  # n일까지 검사
    j = i  # j = n일
    while j < n:
        if j + plan[i][0] > n:  # 현재 일에서 상담일 더했을 때, n일을 넘기면 무시하고 다음날로 이동
            j += 1
            continue
        else:
            dp[i] += plan[j][1]  # 아니라면 n일 최댓값 자리에 비용 더해주기
            j += plan[j][0]  # 상담일 만큼 일 이동

print(max(dp))
