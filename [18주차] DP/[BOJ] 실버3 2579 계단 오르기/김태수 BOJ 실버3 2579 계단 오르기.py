import sys
input = sys.stdin.readline

# 입력받기
n = int(input())
# 입력받는 리스트하나, dp용 리스트하나
arr = [0] * 301
dp = [0] * 301

# 1부터 입력받기
for i in range(1, n + 1):
    arr[i] = int(input())

# 규칙찾아
dp[1] = arr[1]
dp[2] = arr[1] + arr[2]
dp[3] = max(arr[1] + arr[3], arr[2] + arr[3])
for i in range(4, n + 1):
    dp[i] = max(dp[i - 3] + arr[i - 1] + arr[i], dp[i - 2] + arr[i])

# 정답출력
print(dp[n])