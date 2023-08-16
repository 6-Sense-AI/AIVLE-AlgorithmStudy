# 1초동안 미세먼지 확산 -> 공기청정기 작동 일어남
# 미세먼지 확산 : 상하좌우로 확산됨
# 공기청정기 작동 : 위쪽은 반시계, 아래쪽은 시계방향으로 미세먼지 이동, 공기청정기로 들어오면 사라짐

import sys
input = sys.stdin.readline

numR, numC, sec = map(int, input().split())
# room = [list(map(int, input().split())) for _ in range(numR)]
dust_info = []    # 미세먼지가 존재하는 위치
air_info = []    # 공기청정기가 존재하는 위치

for r in range(numR):
    list_r = list(map(int, input().split()))
    for c, n in enumerate(list_r):
        # 공기청정기일 때
        if n < 0:
            air_info.append((r, c))
        # 미세먼지가 존재할 때
        if n > 0:    
            dust_info.append(((r, c), n))

# 미세먼지의 확산 방향 (상하좌우)
moveR = [-1, 1, 0, 0]
moveC = [0, 0, -1, 1]

# 시간초만큼 반복
for _ in range(sec):
    # 미세먼지 확산
    for (r, c), dust in dust_info:
        for dr, dc in zip(moveR, moveC):
            if (0 <= dr < numR) and (0 <= dc < numC):
                

    # 공기청정기 작동
    for (r, c), dust in dust_info:
        print()
# 1. 미세먼지가 확산된다. 확산은 미세먼지가 있는 모든 칸에서 동시에 일어난다.
# (r, c)에 있는 미세먼지는 인접한 네 방향으로 확산된다.
# 인접한 방향에 공기청정기가 있거나, 칸이 없으면 그 방향으로는 확산이 일어나지 않는다.
# 확산되는 양은 Ar,c/5이고 소수점은 버린다.
# (r, c)에 남은 미세먼지의 양은 Ar,c - (Ar,c/5)×(확산된 방향의 개수) 이다.

# 2. 공기청정기가 작동한다.
# 공기청정기에서는 바람이 나온다.
# 위쪽 공기청정기의 바람은 반시계방향으로 순환하고, 아래쪽 공기청정기의 바람은 시계방향으로 순환한다.
# 바람이 불면 미세먼지가 바람의 방향대로 모두 한 칸씩 이동한다.
# 공기청정기에서 부는 바람은 미세먼지가 없는 바람이고, 공기청정기로 들어간 미세먼지는 모두 정화된다.

# 방에 남아있는 미세먼지의 양 계산
total_dust = 0
for _, d in dust_info:
    total_dust += d

print(total_dust)    # 결과 출력