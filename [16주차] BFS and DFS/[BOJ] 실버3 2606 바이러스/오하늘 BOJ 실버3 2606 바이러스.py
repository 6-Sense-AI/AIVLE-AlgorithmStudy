import sys
from collections import deque
input = sys.stdin.readline

# bfs로 풀이 

com = int(input())
m = int(input())
visited = [False] * (com+1)
g = [[] for i in range(com+1)]
cnt = 0

for i in range(m):
    a, b = map(int, input().split())
    g[a].append(b)
    g[b].append(a)

q = deque([1])
visited[1] = True
    
while q:
    a = q.popleft()
    cnt += 1
    for i in g[a]:
        if not visited[i]:
            q.append(i)
            visited[i] = True

print(cnt -1 ) #1번 컴퓨터 제외
