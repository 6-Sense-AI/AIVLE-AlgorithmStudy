import sys
from collections import deque
input = sys.stdin.readline

t = int(input())    # 테스트 케이스의 수

for _ in range(t):

    ncols, nrows, k = map(int, input().split())    # 가로, 세로 길이, 배추가 심어져 있는 위치의 수
    grid = [[0] * ncols for _ in range(nrows)]    # 배추가 심어져 있는 위치의 정보

    # 배추가 심어져 있는 위치 정보 입력 받기
    for _ in range(k):
        c, r = map(int, input().split())
        grid[r][c] = 1

    splt = 0    # 배추가 심겨진 구역수
    # 방문여부 리스트
    visited = [[False] * ncols for _ in range(nrows)]
    # 이동 가능한 경로
    moveR = [0, 0, -1, 1]
    moveC = [-1, 1, 0, 0]

    # 배추가 모여 있는 구역의 수 구하는 함수
    def bfs(sr, sc):
        q = deque([(sr, sc)])
        visited[sr][sc] = True

        # 연결된 모든 노드 탐색
        while q:
            nr, nc = q.popleft()    # 큐에서 값 꺼내기

            # 이동 시키기
            for dr, dc in zip(moveR, moveC):
                nowR = nr + dr
                nowC = nc + dc

                if (0 <= nowR < nrows) and (0 <= nowC < ncols):    # 범위를 넘어가지 않고,
                    if not visited[nowR][nowC] and grid[nowR][nowC] > 0:    # 방문한 적이 없고, 배추가 심어진 곳이라면
                        q.append((nowR, nowC))
                        visited[nowR][nowC] = True

    for i in range(nrows):
        for j in range(ncols):
            if grid[i][j] > 0 and not visited[i][j]:    # 배추가 심겨진 곳이고, 방문 전이라면
                splt += 1    # 구역수 늘려주기
                bfs(i, j)    # 연결된 구역 탐색

    # 결과 출력
    print(splt)               
