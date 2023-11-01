import sys
from collections import deque
# 빗물이 고일 수 있는 조건은 자기 기준으로 양옆이 자기보다 크면 무조건 쌓임
# 미완..
input = sys.stdin.readline

H,W = map(int, input().split())

h_lst = list(map(int, input().split()))

water = 0

walls = []

for i,h in enumerate(h_lst):
    if i == 0 or i == W-1:
        walls.append((i,h))
    else:
        if walls[-1][1] <= h:
            walls.append((i,h))

for left,right in zip(walls[:-1],walls[1:]):
    for idx in range(left[0],right[0]):
        wall = min(left[1],right[1])
        if wall >= h_lst[idx]:
            water += wall - h_lst[idx]

print(water)