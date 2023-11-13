# 구름 visited 함수 만들어서 시간초과 해결

n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]    # 칸의 정보
moves = [list(map(int, input().split())) for _ in range(m)]    # 이동 정보
dirs = [(0, -1), (-1, -1), (-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1)]    # ←, ↖, ↑, ↗, →, ↘, ↓, ↙
clouds = [(n-1, 0), (n-1, 1), (n-2, 0), (n-2, 1)]     # 구름의 위치 정보

# 물복사 시전 함수 (대각선에 물이 존재하는지 확인)
def copy_water(r, c):
    cnt = 0    # 물이 존재하는 위치의 수
    for dr, dc in [(-1, -1), (-1, 1), (1, -1), (1, 1)]:
        mr, mc = r + dr, c + dc
        if 0 <= mr < n and 0 <= mc < n:
            if grid[mr][mc]:
                cnt += 1

    return cnt

for d, step in moves:
    d -= 1
    visited = [[False] * n for _ in range(n)]

    # 구름 이동, 물 내리기
    for i in range(len(clouds)):
        r, c = clouds[i]
        dr, dc = dirs[d]
        r = (n + r + dr * step) % n
        c = (n + c + dc * step) % n

        clouds[i] = (r, c)    # 구름 이동
        visited[r][c] = True
        grid[r][c] += 1    # 물 내리기

    # 물복사 시전
    for i in range(len(clouds)): 
        r, c = clouds[i]
        grid[r][c] += copy_water(r, c)    

    # 바구니에 저장된 물의 양이 2 이상인 모든 칸에 구름이 생기고, 물의 양이 2 줄어든다. 
    tmp = set()
    for i in range(n):
        for j in range(n):
            if grid[i][j] >= 2 and not visited[i][j]:
                grid[i][j] -= 2
                tmp.add((i, j))
    clouds = list(tmp)

print(sum(sum(grid, [])))