n = int(input())


## 기간이랑 수익을 table로 받아오기

for _ in range(n):

    table = list(map(int,input().split()))
    
dp = [0]*(n+1)

## i번째 날에 상담을 하게 되면 그 날에서 시작해서 상담 기간을 더한 날부터 상담이 가능

## j번째 날이 탐색 시작하는 날보다 수익이 작다면 dp[j]값을 바꿔준다.

for i in range(n+1):
    for j in range(i + table[i][0], n+1):
        if dp[j] < dp[i] + table[i][1]:
            dp[j] = dp[i] + table[i][1]

# 가장 뒤에 있는 값이 최대값?
print(dp[-1])

## int subscri 어쩌구 
