

## 하루에 X보다 먼 거리를 걷지 않고 거리가 가까운 집부터 방문
## 왕복할 수 없는 거리는 다음날 가기
## N-1개의 이웃집 모두에게 떡을 돌리기 위해서는 최소 며칠이 소요
## 모두 방문할수 없으면 -1을 출력




##  집 개수 (0부터 n-1), 양방향 도로 개수, 최대 이동 거리, 시작 지점 입력
n, m, x, y = map(int,input().split())  

import heapq



graph = [[] for _ in range(m+1)]

## 양방향 도로 연결 정보 입력
for _ in range(m):
    a, b, c = map(int, input().split())
  
    graph[a].append([b, c])
    graph[b].append([a, c])
    



def dijkstra():
    distances = [float("inf")]*(n)
    distances[y] = 0
    q = []
    heapq.heappush(q, [0, y])


    ## 현재까지 최소 거리와 노드를 꺼내와서 비교
    while q:
        
        cnt_distance, node = heapq.heappop(q)
        
        
        if distances[node] < cnt_distance:
            continue
        
        for adjacency_node, distance in graph[node]:
            cal_distance = distances[node] + distance
            
            if cal_distance < distances[adjacency_node]:
                distances[adjacency_node] = cal_distance
                heapq.heappush(q, (cal_distance, adjacency_node))
        
                
    return distances


distances = dijkstra()
distances_idx = [[distance, idx] for idx, distance in enumerate(distances)]
distances_idx.sort()


## 거리의 2배를 했을 때 x보다 크면 모두 방문 불가능

if distances_idx[-1][0] * 2 > x: 
    print(-1)
    

## 총 이동 거리를 x랑 비교
     
else:
    day = 1
    cur = 0
    for distance, idx in distances_idx:
        if cur + 2 * distance <= x:
            cur += 2 * distance
        else:
            day += 1
            cur = 2 * distance
    print(day)