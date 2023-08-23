# 짱관 감사합니다 정말 ppt를 잘 만드셨군요

import sys
from collections import defaultdict
import heapq

input = sys.stdin.readline
INF = int(10**9)

v, e = map(int, input().split())

k = int(input())

graph = defaultdict(list)

for _ in range(e):
    st,ed,w = map(int, input().split())
    graph[st].append([ed,w])

distance = [INF]*(v+1)

def djikstra(start):
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0

    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue

        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))

djikstra(k)

for i in range(1,v+1):
    if distance[i] == INF:
        print('INF')
    else:
        print(distance[i])





# def bfs(graph, start, target):
#     if target == start:
#         return 0
#     cnt = 0
#     que = deque([[start,0]])
#     cost = 1000
#     graph_ = copy.deepcopy(graph)
#     while que:
#         node,c = que.popleft()
#         for g in graph_[node]:
#             if g[0] == target:
#                 cnt += g[1] + c
#                 cost = min(cost,cnt)
#                 break
#             else:
#                 que.append(g)
#     return cost


# for i in range(1,v+1):
#     cost = bfs(graph, k, i)
#     if cost != 1000:
#         print(cost)
#     else:
#         print('INF')
