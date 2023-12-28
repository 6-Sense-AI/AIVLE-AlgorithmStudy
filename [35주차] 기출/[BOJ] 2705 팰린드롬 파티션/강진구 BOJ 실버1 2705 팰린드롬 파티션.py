import sys

input = sys.stdin.readline

t = int(input())

for _ in range(t):
    n = int(input())

    dp = [1,2,2,4,4]

    if n<=len(dp):
        print(dp[n-1])
    
    else:
        for i in range(len(dp),n):
            if i//2:# 이 부분의 코드는 이해가 안간다. i%2==0이랑 같은 의미가 아닌가? i%2==0으로 제출하면 틀렸다고 나온다.
                dp.append(dp[(i-1)//2] + dp[i-2])
            else:
                dp.append(dp[i-1] + 2)
        
        print(dp[n-1])
