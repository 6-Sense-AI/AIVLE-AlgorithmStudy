import sys
input = sys.stdin.readline

# 입력받기
n, m = map(int,input().split())
num = list(map(int,input().split()))

cnt = 0
sum = 0
end = 0

# 차례대로 증가시키기
for start in range(n):
    # end 조건(범위 지키기)
    while sum < m and end < n:
        sum += num[end]
        end += 1
    if sum == m:
        cnt += 1
    sum -= num[start]

print(cnt)