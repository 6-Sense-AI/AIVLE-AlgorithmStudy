import sys
input = sys.stdin.readline
n = int(input())
a, b = map(int, input().split())

visited = [False] * (n+1)
graph = [[] for _ in range(n+1)]
num = int(input())
for _ in range(num):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)

def dfs(a, b, num):
    visited[a] = True
    if a == b:
        cnt = num
    for i in graph[a]:
        if not visited[i]:
            dfs(i, b, num+1)
    return cnt
