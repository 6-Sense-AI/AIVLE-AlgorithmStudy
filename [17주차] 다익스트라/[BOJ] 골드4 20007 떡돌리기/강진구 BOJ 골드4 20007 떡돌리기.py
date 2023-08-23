import sys
from collections import defaultdict, deque

input = sys.stdin.readline

n, m ,limit, home = map(int, input().split())

graph = defaultdict(list)

for _ in range(m):
    st, end, dist = map(int, input().split())
    graph[st].append((end, dist))
    graph[end].append((st, dist))

visit = [0 for _ in range(n)]

def bfs(graph, visit, start):
    que = deque([start])
    visit[start] = 1
    l = 0
    day = 1
    while que:
        node = que.popleft()

        for n, dist in graph[node]:
            if visit[n] == 0 and l+dist*2<=limit:
                que.append(n)
                l += dist*2
                visit[n] = 1
            elif visit[n] == 0 and l+dist*2>limit:
                day += 1
                l -= 21
                l += dist*2
                visit[n] = 1
                que.append(n)
            elif dist*2>limit:
                break
    return day

day = bfs(graph, visit, home)

if 0 in visit:
    print(-1)
else:
    print(day)
