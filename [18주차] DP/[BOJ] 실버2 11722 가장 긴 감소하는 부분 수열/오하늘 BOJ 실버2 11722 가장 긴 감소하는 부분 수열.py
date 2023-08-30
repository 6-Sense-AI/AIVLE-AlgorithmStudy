import sys
input = sys.stdin.readline

n = int(input()) # 배열길이
arr = list(map(int, input().split())) # 배열

dp = [1] * n # dp는 수열의 길이로 갱신해줌

for i in range(n):
    for j in range(i):
        if arr[j] > arr[i] : # 다음 값보다 크다면
            dp[i] = max(dp[i], dp[j]+1) # 기존, 갱신

print(max(dp))