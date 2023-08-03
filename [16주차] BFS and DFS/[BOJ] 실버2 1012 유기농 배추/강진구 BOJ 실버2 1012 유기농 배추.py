import sys

sys.setrecursionlimit(10**6)
input = sys.stdin.readline

t = int(input())

cnt_lst = []

def dfs(graph, r, c, m, n):
    dr = [1,-1,0,0]
    dc = [0,0,1,-1]
    
    for i in range(4):
        nr = r+dr[i]
        nc = c+dc[i]
        
        if (nr<0) or (nr>=n) or (nc<0) or (nc>=m):
            continue

        if graph[nr][nc] == 1:
            graph[nr][nc] = 0
            dfs(graph, nr, nc, m, n)
        
        
    

for _ in range(t):
    m,n,k = map(int, input().split())

    graph = [[0 for _ in range(m)] for _ in range(n)]
    p = []

    for _ in range(k):
        c,r = map(int, input().split())
        p.append((r,c))
        graph[r][c] += 1

    cnt = 0

    for r,c in p:
        if graph[r][c] == 1:
            dfs(graph, r, c, m, n)
            cnt += 1
        else:
            continue

    cnt_lst.append(cnt)

for c in cnt_lst:
    print(c)