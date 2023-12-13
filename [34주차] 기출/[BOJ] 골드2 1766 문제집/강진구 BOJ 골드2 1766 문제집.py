import sys
import heapq

input = sys.stdin.readline

n,m = map(int, input().split())

graph = [[] for _ in range(n+1)]

indegree = [0]*(n+1)

for _ in range(m):
    a,b = map(int, input().split())
    graph[a].append(b)
    indegree[b] += 1

res = []

q = []

for i in range(1,n+1):
    if indegree[i] == 0:
        heapq.heappush(q, i)

while q:
    now = heapq.heappop(q)
    res.append(now)
    
    for g in (graph[now]):
        indegree[g] -= 1
        if indegree[g] == 0:
            heapq.heappush(q, g)

for r in res:
    print(r, end=' ')