# 빨강, 초록을 하나의 구역으로 볼 때 / 빨, 파, 초를 각각의 구역으로 볼 때
import sys
from collections import deque
input = sys.stdin.readline

n = int(input())    # 그리드의 크기
grid = [list(input().rstrip()) for _ in range(n)]    # 그리드의 색정보

# 연결할 수 있는 방향 정보 (상하좌우)
moveR = [-1, 1, 0, 0]
moveC = [0, 0, -1, 1]

# 컬러별 구역 수 구하는 함수
# start: 탐색 시작 위치 튜플, splt_colors: 같은 색으로 구분할 색 리스트
def find_split(start, splt_colors, visited):

    # 큐 선언
    q = deque([(start[0], start[1])])
    visited[start[0]][start[1]]

    while q:
        r, c = q.popleft()

        for dr, dc in zip(moveR, moveC):
            mr = r + dr
            mc = c + dc

            if (0 <= mr < n) and (0 <= mc < n):
                if not visited[mr][mc] and grid[mr][mc] in splt_colors:
                    q.append((mr, mc))
                    visited[mr][mc] = True

# 적록색약 구역의 수, 방문 여부 리스트
c2_splt = 0
c2_visited = [[False] * n for _ in range(n)]

# 적록색약 X 구역의 수, 방문 여부 리스트
c3_splt = 0
c3_visited = [[False] * n for _ in range(n)]

# 전체 그리드 확인
for i in range(n):
    for j in range(n):

        # 적록색약 구역 수 구하기
        if grid[i][j] in ('R', 'G') and not c2_visited[i][j]:
            c2_splt += 1
            find_split((i, j), ('R', 'G'), c2_visited)
        if grid[i][j] == 'B' and not c2_visited[i][j]:
            c2_splt += 1
            find_split((i, j), ('B'), c2_visited)

        # 적록색약 X 구역 수 구하기
        for c in ('R', 'G', 'B'):
            if grid[i][j] == c and not c3_visited[i][j]:
                c3_splt += 1
                find_split((i, j), (c), c3_visited)

# 결과 출력
print(c3_splt, c2_splt)