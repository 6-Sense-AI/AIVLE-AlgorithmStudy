# 나는 멍청이~
# 고쳤으요!

import sys
from collections import defaultdict, deque

input = sys.stdin.readline

n = int(input())

a,b = map(int, input().split())

m = int(input())
graph = defaultdict(list)

for _ in range(m):
    k,v = map(int, input().split())
    graph[k].append(v)
    graph[v].append(k)

visited = [False]*n
cnt = 0
que = deque([(a,b,cnt)])

while que:
    st,ed,cnt = que.popleft()
    visited[st-1] = True
    
    if ed in graph[st]:
        cnt += 1
        st = ed
        break
    else:
        for g in graph[st]:
            if visited[g-1]==False:
                que.append((g,ed,cnt+1))
            else:
                continue
        
if st != ed:
    cnt = -1
print(cnt)

    
    
