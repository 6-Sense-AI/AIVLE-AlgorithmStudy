from collections import deque
import sys
input = sys.stdin.readline

# BFS 함수
def bfs(graph, visited, tr, tc):
    
    move = [[-1, 0], [1, 0], [0, -1], [0, 1]]    # 이동할 수 있는 경우의 수 (상, 하, 좌, 우)
    
    # 1. queue 선언 및 방문 처리
    queue = deque([(0, 0, 0)])
    visited[0][0] = True
    
    # 2. 큐가 빌 때까지 반복
    while queue:
        # 3. 큐에서 요소 빼서 출력
        r, c, cnt = queue.popleft()
        
        # 4. 목표 위치에 도달했으면, 종료
        if r == (row - 1) and c == (col - 1):
            return cnt
        
        # 5. 움직일 수 있는 모든 경우의 수 저장
        canmove = []
        for m in move:
            a = r + m[0]
            b = c + m[1]
            if (a >= tr) or (a < 0) or (b >= tc) or (b < 0):    # 범위를 벗어나면, 저장 X
                continue
            canmove.append([a, b])
        
        # 6. 이동 가능한 모든 경우의 수 방문
        for nxt in canmove:
            # 7. 방문하지 않았다면, queue에 삽입 및 방문 처리
            if not visited[nxt[0]][nxt[1]] and graph[nxt[0]][nxt[1]] == 1:    
                queue.append((nxt[0], nxt[1], cnt + 1))
                visited[nxt[0]][nxt[1]] = True
                
# row, col: 이동할 끝좌표
row, col = map(int, input().split())
mapli = []

for r in range(row):
    str = list(input().strip())
    
    mapli.append(list(map(int, str)))
    
visited = [[False] * col for _ in range(row)]

print(bfs(mapli, visited, row, col) + 1)