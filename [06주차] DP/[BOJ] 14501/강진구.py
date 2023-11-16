import sys

input = sys.stdin.readline

n = int(input())

dp = [0]*(n+1)
schedule = []

for _ in range(n):
    schedule.append(tuple(map(int,input().split())))

for i,t in enumerate(schedule):
    if i+t[0] < n+1:    # 날짜와 걸리는 기간이 n일까지 될때
        dp[i+t[0]] = max(t[1]+max(dp[:i+1]),dp[i+t[0]])   
        # 상담이 끝나는 날을 여지껏 했던것을 기준으로 제일 큰 값과 앞으로 더해지는 값 vs 원래 그 자리에 있던 값 중 큰 값을 넣어줌
        
print(max(dp)) # dp에서 제일 큰 값을 뽑아줌
