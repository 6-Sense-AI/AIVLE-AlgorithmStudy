import heapq
import sys




## 입력받기
INF = int(1e9)
short_num, gosok_dist = map(int, sys.stdin.readline().split())

## 지름길 
graph = [[] for i in range(short_num+1)]

## 지름길 입력받기
for i in range(short_num+1):
    start, finish, short_dist = map(int,sys.stdin.readline().split())
    
    graph[start].append((finish, short_dist))
    


## 비용 전체 INF로 초기화
distance = [INF] * (short_num+1)



## 세준이는 0부터 출발해 gosok_dist까지 간다.
## 0~gosok_dist +1 까지 for문 반복
## graph[start]에 걸리는 지점 있으면 최소값을 answer에 더하고
## 전체 거리 gosok_dist에서 (finish - start)를 빼 주면서 gosok_dist 갱신
## 다 돌리고 마지막에 answer + gosok_dist 반환

short_list = []  
def dijkstra(start):
    q = []
    
    ## 거리, 시작 지점 큐에 삽입
    heapq.heappush(q,(0,start))
    
    ## 시작지점 비용 초기화
    distance[start] = 0
    
    ## heap을 이용해 q에서 최소값 반환
    ## 
    
    
    while q:
        dist, now = heapq.heappop(q)
        
        ## 처음 주어진 직선 거리보다 계산한 값이 클 경우 패스
        if distance[now] < dist:
            continue
        for i in graph[now]:
            cost = dist + i[1]
            
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                
                heapq.heappush(q, (cost,i[0]))
              
dist_list = dijkstra(0)  ## 가장 짧은 지름길 리스트 출력
answer = 0    
total = gosok_dist
for loc in range(1, gosok_dist+1):
    for j in range(len(short_list)):
        if loc == short_list[j]:
            answer +=dist_list[j]
            total -= loc
print(answer + total)
