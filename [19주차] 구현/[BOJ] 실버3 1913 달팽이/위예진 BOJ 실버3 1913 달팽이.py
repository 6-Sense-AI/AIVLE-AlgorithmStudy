n = int(input())    # 행,열의 크기
s = int(input())    # 위치를 찾고자 하는 자연수

# 이동하는 순서 (하, 우, 상, 좌)
moveR = [1, 0, -1, 0]
moveC = [0, 1, 0, -1]

grid = [[False] * n for _ in range(n)]    # N x N의 정사각형
nr, nc, m = 0, 0, 0    # 현재 위치
for i in range(n * n, 0, -1):
    grid[nr][nc] = i

    # 이동
    mr = nr + moveR[m]
    mc = nc + moveC[m]
    if 0 <= mr < n and 0 <= mc < n:    # 범위를 벗어나지 않고,
        if not grid[mr][mc]:    # 아직 채워진 적 없다면,
            nr, nc = mr, mc    # 이동
        else:
            m = (m + 1) % 4
            nr += moveR[m]
            nc += moveC[m]
    else:
        m = (m + 1) % 4
        nr += moveR[m]
        nc += moveC[m]

# 완성된 달팽이 출력
for i in range(n):
    print(*grid[i])

# 찾는 숫자의 위치 출력
for i in range(n):
    if s in grid[i]:
        print(i+1, grid[i].index(s) + 1)