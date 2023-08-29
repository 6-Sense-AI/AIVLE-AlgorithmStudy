n = int(input())
a = list(map(int, input().split()))
dp = [1 for _ in range(n)]  # 최댓값

for i in range(n):
    for j in range(i):  # 현재값 이전 값들 검사
        if a[j] > a[i]:  # 조건이 만족할 때
            dp[i] = max(dp[i], dp[j] + 1)  # 최대값 갱신

print(max(dp))
