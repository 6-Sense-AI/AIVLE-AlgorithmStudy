# 5383. 떡 하나 주면 안 잡아먹지
from collections import deque
import sys
input = sys.stdin.readline

# bfs 함수 구현
def bfs(graph, visited, target):
    
    # 이동할 수 있는 종류 (상, 하, 좌, 우)
    mr = [-1, 1, 0, 0]
    mc = [0, 0, -1, 1]
    
    # 큐 선언 및 방문 처리
    q = deque([(0, 0, graph[0][0])])
    visited[0][0] = True
    
    # 큐가 빌 때까지 인접 노드 방문
    while q:
        # 큐에서 노드 꺼내기
        r, c, ddnum = q.popleft()
        
        # 목표 지점 도달 시, 종료
        if (r == target - 1) and (c == target - 1):
            return(ddnum + graph[r][c])
        
        # 방문 가능한 모든 경우의 수 확인
        for moveR, moveC in zip(mr, mc):
            row = r + moveR
            col = c + moveC
            
            tmp = []
            # 범위를 넘어가지 않고, 방문하지 않았다면, tmp에 저장하고 방문처리
            if (row >= 0 and row <= target - 1) and (col >= 0 and col <= target - 1) and not visited:
                tmp.append((row, col, ddnum + graph[row][col]))
                visited[row][col] = True
                
            # 떡의 수가 적은 순서대로 정렬 후, q에 넣기
            tmp = sorted(tmp, key=lambda x: x[2])
            for t in tmp:
                q.append(t)

n = int(input())    # (n * n) 행렬의 n
ddli = []    # 호랑이 지도
for _ in range(n):
    ddli.append(list(map(int, input().split())))
    
print(ddli)
# 방문 여부 리스트 초기화
visited = [[False] * n for _ in range(n)]
print(bfs(ddli, visited, n))