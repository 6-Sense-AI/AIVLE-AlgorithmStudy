from collections import deque

def dfs(graph, v, visited):

    ## 방문 노드 표시
    visited[v] = True
    print(v, end= ' ')

    ## 미방문 노드는 dfs 재귀
    ## 작은 숫자부터 찾아 나가게 만들었다
    for i in graph[v]:
        if not visited[i]:
            dfs(graph,i,visited)


## stack을 사용하는 dfs와 달리 bfs는 queue를 사용한다.
## 따라서 popleft로 노드를 계속 빼면서 queue가 완전히 빌 때까지 반복한다.

def bfs(graph, v, visited):

    queue = deque([v])
    ## 방문 노드 표시
    visited[v] = True
    
    while queue:
        ## 밑에서 하나씩 노드 뽑기
        v = queue.popleft() 
        print(v, end = ' ')

        ## 미방문 노드 
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True



n, m, v = map(int, input().split())  ## 정점 개수, 간선 개수, 시작 정점 번호 입력

graph = [[] for _ in range(n+1)]

for _ in range(m):
    a, b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)


visited = [False]*(n+1)

dfs(graph, v, visited)
print()
visited = [False] * (n+1)

bfs(graph,v,visited)
print()