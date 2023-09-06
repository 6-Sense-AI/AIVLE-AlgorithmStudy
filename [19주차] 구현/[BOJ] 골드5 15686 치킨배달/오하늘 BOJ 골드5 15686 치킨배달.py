import sys
input = sys.stdin.readline

n, m = map(int, input().split()) #도시의 정보, 치킨집 수
arr = [list(map(int,input().split())) for i in range(n)] # 도시 맵

home = [] # 집
ck = [] # 치킨
for i in range(n):
    for j in range(n):
        if arr[i][j] == 1: home.append((i,j))
        if arr[i][j] == 2: ck.append((i,j))

# 생각한 전략
# 주어진 치킨집 수를 z라고 할떄 에서 m개 즉 zCm의 조합을 돌려서
# 제일 적은 수의 값을 도출하면 된다.

# 문제는 조합을 어떻게 구하지 ??? -> 결국 구글 봄
# 파이썬에서 combination 메소드를 이용하면 된다고 한다.
from itertools import combinations # 조합 임포트

# 도시의 치킨 거리 구하기
def ck_dist(home, ck):
    dist = 0
    for i, j in home: # 집에서
        temp = int(1e9)
        for i2, j1 in ck:
            temp = min(temp, abs(i2-i) + abs(j1-j)) # abs는 절대값 메소드
        dist += temp
    return dist


# 치킨 집 조합 별로 최소 구하기
result = float("inf")
for i in combinations(ck, m): # 치킨집에서 m 구하기
    result = min(result, ck_dist(home, i))

print(result)