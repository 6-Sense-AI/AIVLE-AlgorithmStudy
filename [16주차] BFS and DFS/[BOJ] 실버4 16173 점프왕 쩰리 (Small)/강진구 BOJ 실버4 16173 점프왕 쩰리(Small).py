import sys

sys.setrecursionlimit(10**9)

n = int(input())

def dfs(graph, r, c):
    if r<=-1 or r>=n or c<=-1 or c>=n or visited[r][c]==True:
        return 
    
    if graph[r][c] == -1:
        visited[r][c] = True
        return 
    
    visited[r][c] = True

    dfs(graph, r+graph[r][c], c)
    dfs(graph, r, c+graph[r][c])


graph = [list(map(int, input().split())) for _ in range(n)]

visited = [[False]*n for _ in range(n)] # [[]*n]*n 으로 만들어 봤는데 안되서 찾아보니 곱하기로 만들면 복제라 바뀔 때 한번에 바뀜

dfs(graph, 0, 0)
if visited[-1][-1] == True:
    print('HaruHaru')
else:
    print('Hing')
