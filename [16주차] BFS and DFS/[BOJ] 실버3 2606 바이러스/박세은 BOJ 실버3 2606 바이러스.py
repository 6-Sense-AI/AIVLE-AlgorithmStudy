from collections import deque

n = int(input()) # 컴퓨터 수
m = int(input()) # 네트워크 연결 수

grp = [[False] * (n + 1) for _ in range(n + 1)]

for _ in range(m):
    a, b = map(int, input().split())
    grp[a][b] = True
    grp[b][a] = True

visited = [False] * (n+1)
cnt = [] # 1번 컴퓨터와 연결된 컴퓨터들 저장 리스트

def bfs(start):
    que = deque([start]) 
    visited[start] = True # 시작 노드 방문처리

    while que:
        start = que.popleft() 
        for i in range(1, n+1):
            if not visited[i] and grp[start][i]: # 방문하지 않았으며 시작 노드와 연결돼있다면
                cnt.append(i) # 리스트에 해당 컴퓨터 저장
                que.append(i) # 큐에 삽입
                visited[i] = True # 방문처리

bfs(1)
print(len(cnt))



