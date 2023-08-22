## 감이 안잡혀서 블로그보고 풀어봤음 ##
##================================##
import heapq

INF = int(1e9) # 알 수 없음 값

def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start)) # 시작 정점과 그 정점까지의 거리 큐에 삽입
    distance[start] = 0 # 시작 정점의 거리 0으로 설정
    
    while q: # 큐가 빌 때 까지 반복
        # 현재 거리가 가장 짧은 정점의 정보 가져옴
        dist, now = heapq.heappop(q) # 거리, 현재 정점 번호

        if dist > distance[now]: # 이미 더 짧은 경로로 방문한 경우 건너뜀
            continue

        for i in grp[now]: # 현재 정점에서 이동할 수 있는 모든 인접 정점들에 대해 거리를 갱신
            cost = dist + i[1] # i[0]까지의 거리
            if cost < distance[i[0]]: # 현재 정점을 거치는 거리(cost)와 현재까지의 최단거리를 비교 
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0])) 

n, d = map(int, input().split()) # 지름길 개수, 고속도로 길이
grp = [[] for _ in range(d+1)] # 이동할 수 있는 다른 위치와 그 비용을 나타낸 리스트
distance = [INF] * (d+1) # 최단거리 저장 배열

# 바로 다음 위치로 이동시 1의 비용을 사용하므로 우선 1로 채워줌
for i in range(d):
    grp[i].append((i+1, 1))

# 지름길 있는 경우 업데이트 해주기
for _ in range(n):
    # 시작위치, 도착위치, 길이
    s, e, l = map(int, input().split())
    if e > d: # 도착위치가 고속도로 길이보다 길면 무시
        continue
    grp[s].append((e, l))

dijkstra(0) # 시작 위치에서 모든 위치까지의 최단 거리 계산
print(distance[d]) # 도착위치에 업로드 돼있는 최단거리 출력




