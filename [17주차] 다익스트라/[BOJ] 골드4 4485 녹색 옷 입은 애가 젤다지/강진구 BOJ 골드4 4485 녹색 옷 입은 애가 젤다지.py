import sys

sys.setrecursionlimit(10**9)

input = sys.stdin.readline

INF = int(1e9)

def dfs(graph, visit, start, distance):
    r, c = start
    visit[r][c] = 1
    distance[0][0] = graph[0][0]

    if r==n-1 and c==n-1:
        return distance

    dr = [0,0,1,-1]
    dc = [1,-1,0,0]
    
    for i in range(4):
        nr = r+dr[i]
        nc = c+dc[i]
        
        if 0<=nr<n and 0<=nc<n and visit[nr][nc] == 0:
            if graph[nr][nc]+distance[r][c] < distance[nr][nc]:
                distance[nr][nc] = graph[nr][nc] + distance[r][c]
            dfs(graph, visit, (nr,nc), distance)
        

n = int(input())

while n != 0:
    graph = []
    visit = [[0 for _ in range(n)] for _ in range(n)]
    distance = [[INF for _ in range(n)] for _ in range(n)]
    for _ in range(n):
        graph.append(list(map(int, input().split())))
    
    for _ in range(4):
        c = dfs(graph, visit, (0,0), distance)
    print(distance[-1][-1])
    n = int(input())