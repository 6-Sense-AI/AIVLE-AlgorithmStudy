import sys
input = sys.stdin.readline

# 기간 t와 금액 p의 리스트 형성
n = int(input())
t = [] * (n+1)
p = [] * (n+1)
dp = [0] * (n+1)

# a,b 각각 입력받아 리스트에 넣기
for _ in range(n):
    a, b = map(int,input().split())
    t.append(a)
    p.append(b)

# M은 이전에 저장된 M의 값과 dp[i]중 큰 값으로 갱신한다
# dp[i]는 '현재까지의 수익에 이번 상담의 수익' 을 더한 값과
#         '오늘의 상담이 끝나는 시점의 수익' 중 큰 값을 저장한다.
M = 0
for i in range(n):
    M = max(M, dp[i])
    if i + t[i] > n:
        continue
    dp[i + t[i]] = max(M + p[i], dp[i+t[i]])

print(max(dp))