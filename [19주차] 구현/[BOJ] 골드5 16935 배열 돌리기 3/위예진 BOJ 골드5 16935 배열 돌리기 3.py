import sys
input = sys.stdin.readline

# 배열의 크기: (rows x cols), 연산의 수: n
rows, cols, n = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(rows)]    # 배열
calc_list = list(map(int, input().split()))    # 수행할 연산 종류 리스트
ans = []    # 결과 배열

for cal in calc_list:

    tmp = []
    # 1. 상하 반전
    if cal == 1:
        for r in range(len(grid)-1, -1, -1):
            tmp.append(grid[r])
        grid = tmp.copy()
    # 2. 좌우 반전
    elif cal == 2:
        for r in grid:
            tmp.append(r[::-1])
        grid = tmp.copy()
    # 3. 오른쪽으로 90도 회전
    elif cal == 3:
        for c in zip(*grid):
            tmp.append(c[::-1])
        grid = tmp.copy()
    # 4. 왼쪽으로 90도 회전
    elif cal == 4:
        for c in zip(*grid):
            tmp.append(c)
        grid = tmp[::-1].copy()
    # 5. 4개의 사분면 그룹으로 나눠, 시계 방향으로 1번 이동
    elif cal == 5:
        r = len(grid)
        c = len(grid[0])
        for i in range(r // 2):
            tmp.append(list(grid[i+r//2][:c//2] + grid[i][:c//2]))
        for i in range(r // 2):
            tmp.append(list(grid[i+r//2][c//2:] + grid[i][c//2:]))
        grid = tmp.copy()
    # 6. 4개의 사분면 그룹으로 나눠, 반시계 방향으로 1번 이동
    else:
        r = len(grid)
        c = len(grid[0])
        for i in range(r // 2):
            tmp.append(list(grid[i][c//2:] + grid[i+r//2][c//2:]))
        for i in range(r // 2):
            tmp.append(list(grid[i][:c//2] + grid[i+r//2][:c//2]))
        grid = tmp.copy()

for r in grid:
    print(*r)