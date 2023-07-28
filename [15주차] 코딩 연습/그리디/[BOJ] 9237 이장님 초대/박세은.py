import sys

input = sys.stdin.readline

# 입력 받기

n = int(input()) # 묘목 수
t = list(map(int, input().split())) # 걸리는 시간

# 자라는 속도가 느린 나무부터 처리하기 위해 내림차순 정렬
t.sort(reverse=True) 

# 정렬한 값에 각각 n일만큼의 시간을 더해줌
i = 1

while i <= n :
    t[i-1] += i
    i += 1

# 최대값에 묘목 구입날 1을 더해줌
print(max(t)+1)
