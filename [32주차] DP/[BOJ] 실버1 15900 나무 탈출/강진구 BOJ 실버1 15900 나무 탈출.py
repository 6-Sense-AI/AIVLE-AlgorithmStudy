# dfs로 하니까 중간에 런타임 오류 한번 나서 bfs로 하는 방법을 찾아 했습니다.
import sys
from collections import defaultdict, deque

input = sys.stdin.readline

n = int(input().strip())

graph = defaultdict(list)

for _ in range(n-1):
    a,b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

# 1번 루트노드, 모든 리프노드(자식없는)에 말 하나씩, 루트노드에 도착하면 말 제거, 말이 없어지면 짐
depth_cnt = 0

# que = deque((0,1)) 이렇게 잡으면 런타임 에러남
que = deque()
que.append((0,1))
visit = [False for _ in range(n+1)]
visit[1] = True

while que:
    d, x = que.popleft()
    
    isleaf = True
    for g in graph[x]:
        if visit[g] == False:
            isleaf = False
            visit[g] = True
            que.append((d+1,g))
    
    if isleaf:
        depth_cnt += d

# 각 리프까지 얼마나 걸리는지 거리를 계산하고 다 합쳐서 짝,홀 판단 후 짝이면 짐
if depth_cnt%2 == 0:
    print('No')
else:
    print('Yes')