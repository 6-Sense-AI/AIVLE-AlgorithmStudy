# 알고리즘 까먹어서 블로그 보고 풀었슴당.. #
# ===================================== #
from collections import deque

########## True, False로 연결 여부 구현 ##########

n, m, v = map(int, input().split())

# 탐색시 1부터 시작하기 위해 n+1개씩 만들어줌
grp = [[False] * (n+1) for _  in range(n+1)]

for _ in range(m):
    a, b = map(int, input().split())
    grp[a][b] = True 
    grp[b][a] = True 

visited1 = [False] * (n + 1) # dfs 방문기록
visited2 = [False] * (n + 1) # bfs 방문기록

def bfs(v):
    q = deque([v])
    visited2[v] = True # 정점 방문처리
    while q: # q 가 빌때까지 돎
        v = q.popleft() # 큐의 첫째값 꺼내기
        print(v, end = ' ')
        for i in range(1, n + 1):
            if not visited2[i] and grp[v][i]: # 만약 i번에 방문하지 않았는데, v와 연결돼있다면
                q.append(i) # 큐에 i 값 추가
                visited2[i] = True # i 값 방문처리


def dfs(v):
    visited1[v] = True # 정점 방문처리
    print(v, end = ' ')
    for i in range(1, n+1):
        if not visited1[i] and grp[v][i]:
            dfs(i) # 해당 값으로 dfs를 계속 돈다

dfs(v)
print()
bfs(v)

########## 정점만 저장해서 해결하기 ##########

grp = [[] for _ in range(n + 1)]

for _ in range(m):
    grp[a].append(b)
    grp[b].append(a)

# 문제에 낮은 숫자부터 탐색하라 돼있으니 오름차순 정렬
for i in grp:
    i.sort()

def dfs(start):
    visited[start] = True # 정점 방문처리
    print(start, end = ' ')

    for i in grp[start]:
        if not visited[i]:
            dfs(i)

def bfs(start):
    que = deque([start])
    visited[start] = True
    while que:
        v = que.popleft()
        print(v, end=' ')
        for i in grp[v]:
            if not visited[i]:
                visited[i] = True
                que.append(i)

visited = [False] * (n+1)
dfs(v)
print()
visited = [False] * (n+1)
bfs(v)




