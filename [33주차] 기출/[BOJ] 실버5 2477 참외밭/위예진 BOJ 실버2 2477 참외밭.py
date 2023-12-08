# 생각보다 어려웠던 문제,,,
# 풀이 봄
# 두번씩 나오는 방향 중, 끼어있는 가로 세로의 길이가 움푹 들어간 직사각형의 가로 세로임

import sys
input = sys.stdin.readline

k = int(input())    # 1m^2 당 참위의 수
dir_cnt = [0] * 5    # 각 방향의 등장 횟수
moves = []    # (방향, 이동 거리)
for _ in range(6):
    d, m = map(int, input().split())
    moves.append([d, m])
    dir_cnt[d] += 1

big = 1    # 전체 직사각형 넓이
small = 1    # 파인 직사각형 넓이

for i in range(6):
    d, m = moves[i]

    # 한 번만 등장 -> 전체 직사각형의 가로, 세로 길이
    if dir_cnt[d] == 1:
        big *= m
    # 두 번 등장
    else:
        nxt1 = (i + 1) % 6
        nxt2 = (i + 2) % 6    
        # 뒤의 두번째가 나와 같음 -> 그 사이 값이 파인 직사각형의 가로, 세로 길이
        if d == moves[nxt2][0]:
            small *= moves[nxt1][1]

print((big - small) * k)