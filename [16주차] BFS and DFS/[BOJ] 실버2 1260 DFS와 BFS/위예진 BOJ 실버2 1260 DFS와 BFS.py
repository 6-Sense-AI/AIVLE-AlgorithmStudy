import sys
from collections import deque
input = sys.stdin.readline

# 정점, 간선의 수, 시작 정점 번호
# 번호는 1부터
node, edge, start = map(int, input().split())
graph = [[] for _ in range(node + 1)]
for _ in range(edge):

    # 연결 정보 입력받아 양쪽에 연결해주기
    s, e = map(int, input().split())
    graph[s].append(e)
    graph[e].append(s)

# 번호가 적은 노드부터 방문하기 위해 정렬하기
for i in range(len(graph)):
    graph[i].sort()

# dfs 함수
# v: 시작 노드
def dfs(v, visited):
    # 현재 노드 방문 처리
    visited[v] = True
    print(v, end=' ')

    # 연결된 노드들 재귀적으로 방문
    for i in graph[v]:
        if not visited[i]:
            dfs(i, visited)

# bfs 함수
# v: 시작 노드
def bfs(v):
    visited = [False] * (node + 1)    # 방문여부 확인 리스트
    q = deque([v])    # 큐 선언
    visited[v] = True    # 현재 노드 방문 처리
    
    # 연결된 모든 노드들 확인
    while q:
        n = q.popleft()
        print(n, end=' ')

        for i in graph[n]:
            if not visited[i]:
                q.append(i)
                visited[i] = True

    print()

# dfs, bfs 실행
visited = [False] * (node + 1)    # 방문여부 확인 리스트
dfs(start, visited)
print()
bfs(start)