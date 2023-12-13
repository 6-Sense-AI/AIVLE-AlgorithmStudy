import sys
input = sys.stdin.readline
from collections import deque

n, m = map(int,input().split())
indegree = [0] * (n+1) # 진입차수 0으로 초기화
graph = [[] for i in range(n+1)]

for _ in range(m):
    a, b = map(int,input().split())
    graph[a].append(b)
    indegree[b] += 1 # 진입차수 1추가

def topology_sort():
    result = []
    q = deque()

    for i in range(1, n+1):
        if indegree[i] == 0:
            q.append(i)
    
    while q:
        now = q.popleft()
        result.append(now)
        for i in graph[now]:
            indegree[i] -= 1

            if indegree[i] == 0:
                q.append(i)
    for i in result:
        print(i, end=' ')

topology_sort()