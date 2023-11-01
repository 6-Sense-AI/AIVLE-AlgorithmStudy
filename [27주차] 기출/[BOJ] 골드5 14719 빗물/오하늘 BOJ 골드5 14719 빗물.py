import sys
input = sys.stdin.readline

h, w = map(int,input().split()) # 세로, 가로
g = list(map(int,input().split())) # 블럭 쌓인 높이
ans = 0


# 반복문 돌면서 양쪽에 높은 블록이면 무조건 빗물이 고인다.
# 원래 이중 포문 썼는데,, 좋은 방법있어서 수정
for i in range(1,w-1): # 처음과 끝은 기준이 안됨
    # 왼쪽과 오른쪽 값중 최대를 구해 두 값중 작은 값과 중간 비교
    l = max(g[ :i])
    r = max(g[i+1: ])
    t = min(l,r) 

    if t > g[i]: # 이 값이 현재보다 크면
        ans += t -g[i] # 더해줌

print(ans)