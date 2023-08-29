n = int(input())

# dp = [0 for _ in range(n+1)]

# dp[0] = 1
# dp[1] = 2*n
# dp[-1] = 2


# for i in range(2,n):
#     s = 0
#     for j in range(1,(2*n)-1,2):
#         s += (2*n-(i+j))*2
#     dp[i] = s

# print(sum(dp))

dp = [0 for _ in range(n+1)]

dp[0] = 1
dp[1] = 3

for i in range(2,n+1):
    dp[i] = (dp[i-1]*2 + dp[i-2])%9901

print(dp[n])

'''
1 2
1 4 2
1 6 8 2
1 8 18 12 2
1 10 32 18 8 2
등차수열 식
(2n-(i+1))*2
'''