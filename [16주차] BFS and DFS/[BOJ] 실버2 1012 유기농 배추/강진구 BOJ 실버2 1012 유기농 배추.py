import sys

input = sys.stdin.readline

t = int(input())

cnt_lst = []

def dfs(graph, visited, start):
    r, c = start
    visited[r][c] = True
    
    dr = [1,-1,0,0]
    dc = [0,0,1,-1]
    flag = 0
    for i in range(4):
        if (0 <= r + dr[i] < n):
            nr = r+dr[i]
        else:
            nr = r
        if (0 <= c + dc[i] < m):
            nc = c+dc[i]
        else:
            nc = c
        
        if graph[nr][nc] == 1:
            if visited[nr][nc] == False:
                return dfs(graph, visited, (nr, nc))
        flag += 1
    if flag == 4:
        return
    if visited:
        return

for _ in range(t):
    m,n,k = map(int, input().split())

    graph = [[0 for _ in range(m)] for _ in range(n)]
    visited = [[True for _ in range(m)] for _ in range(n)]
    p = []

    for _ in range(k):
        c,r = map(int, input().split())
        p.append((r,c))
        graph[r][c] += 1
        visited[r][c] = False


    cnt = 0

    for r,c in p:
        if visited[r][c] == False:
            dfs(graph, visited, (r,c))
            cnt += 1
        else:
            continue

    cnt_lst.append(cnt)

for c in cnt_lst:
    print(c)