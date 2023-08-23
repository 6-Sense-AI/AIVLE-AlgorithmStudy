import sys
input = sys.stdin.readline
INF = int(1e9)

import heapq


# 다익스트라 함수
def dijkstra(start):
    q = []
    heapq.heappush(q,(0,start))
    distance[start] = 0
    visited[start] = True

    while q:
        dist, now = heapq.heappop(q) # 거리, 현재
        
        for i in range(4):
            # 사분면 돌아서 있으면 돌릴 생각인데
            # x1 = x + dx[i]
            # y1 = y + dy[i]

            for i in g[now]:
                cost = dist + i[1]

                if cost < distance[i[0]]:
                    distance[i[0]] = cost
                    heapq.heappush(q,(cost,i[0]))
                    visited[i[0]] = True

dx = [-1,1,0,0]
dy = [0,0,-1,1]

while 1:
    a = int(input())
    if a == 0: #종료
        break
    
    arr = []
    for i in range(a):
        arr.append(list(map(int, input().split())))

    g = [[] for i in range(a+1)]
    distance = [INF] * (a+1)
    visited = [False] * (a+1)

    dijkstra(0)

    print(arr)
