

## 퇴사 2

## 맨 뒷 자리는 1은 되어야 경쟁에 낄 수 있다


n = int(input())

t_list = [0 for _ in range(n+1)]
p_list = [0 for _ in range(n+1)]

for i in range(n):
    t_list[i], p_list[i] = map(int, input().split())
    
dp = [0 for _ in range(n+1)]

for i in range(1, n+1):

    ## 직전까지 최대 
    dp[i] = max(dp[i], dp[i-1])

    ## 찐막 상담 언제 끝남? 
    end_date = i + t_list[i] -1

    ## n 이전에 끝나면 당일에 상담할 수 있으니까 이전까지 최대랑 당일수당 더한거랑 비교해보자
    if end_date <n:
        dp[end_date] = max(dp[end_date], dp[i-1]+p_list[i])

print(max(dp))