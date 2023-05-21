# 집은 빨강, 초록, 파랑 중 하나의 색으로 칠해야 한다. 각각의 집을 빨강, 초록, 파랑으로 칠하는 비용이 주어졌을 때, 
# 아래 규칙을 만족하면서 모든 집을 칠하는 비용의 최솟값을 구해보자.
# N번 집의 색은 N-1번 집의 색과 같지 않아야 한다.
# i(2 ≤ i ≤ N-1)번 집의 색은 i-1번, i+1번 집의 색과 같지 않아야 한다.

import sys
input = sys.stdin.readline

n = int(input())    # 집의 수
house = [list(map(int, input().split())) for _ in range(n)]    # 각 집의 R, G, B 비용
for i in range(1, n):
    house[i][0] += min(house[i-1][1], house[i-1][2])    # 현재 R 선택, 이전에 G, B 선택 중 최소
    house[i][1] += min(house[i-1][0], house[i-1][2])    # 현재 G 선택, 이전에 R, B 선택 중 최소
    house[i][2] += min(house[i-1][0], house[i-1][1])    # 현재 B 선택, 이전에 R, G 선택 중 최소

print(min(*house[n-1]))