
## 가장 긴 감소하는 부분 수열


a = int(input())

arr = list(map(int,input().split()))

## 길이는 기본 1 보장
dp = [1] * a

## 앞 숫자보다 작으면 감소 부분 수열
for i in range(1, a):
    for j in range(i):
        if arr[j] > arr[i]:
            dp[i] = max(dp[i], dp[j] + 1)

print(max(dp))
 