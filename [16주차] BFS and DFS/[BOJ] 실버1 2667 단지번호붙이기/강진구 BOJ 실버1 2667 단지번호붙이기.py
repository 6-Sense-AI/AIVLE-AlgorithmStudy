import sys
sys.setrecursionlimit(10**9)

input = sys.stdin.readline

n = int(input())

graph = []

for _ in range(n):
    lst = list(input().strip())
    graph.append(lst)

a_lst = []
for i in range(n):
    for j in range(n):
        if graph[i][j] == '1':
            a_lst.append((i,j))

def dfs(graph, row, col):
    global cnt
    if graph[row][col] == '0':
        return cnt
    else:
        graph[row][col] = '0'
        cnt += 1
    dr = [0,0,1,-1]
    dc = [1,-1,0,0]
    for i in range(4):
        nr = row+dr[i]
        nc = col+dc[i]

        if 0<=nr<n and 0<=nc<n and graph[nr][nc]=='1':
            dfs(graph, nr, nc)
        if i==3:
            return cnt
    return cnt
    

c_lst = []
for i,j in a_lst:
    cnt = 0
    if dfs(graph, i, j) != 0:
        c = dfs(graph, i, j)
        c_lst.append(c)


print(len(c_lst))
for i,c in enumerate(sorted(c_lst)):
    print(c)
