# 촌수계산
import sys
from collections import deque
input = sys.stdin.readline

n = int(input()) #사람 수
p1, p2 = map(int, input().split())
k = int(input())

g = [[] for i in range(n+1)] # 친척

visited = [0] * (n+1)

for i in range(k): # 촌수 정보
    a, b = map(int, input().split())
    g[a].append(b)
    g[b].append(a)
    g[a].sort()
    g[b].sort()
    
    
def bfs(p1):
    q = deque([p1])
    flag = 0
    while q:
        v = q.popleft()
        for i in g[v]:
            if visited[i] == False:
                visited[i] = visited[v]+1
                q.append(i)
    
bfs(p1)
if visited[p2] == 0:
    print (-1)
else:
    print(visited[p2])
