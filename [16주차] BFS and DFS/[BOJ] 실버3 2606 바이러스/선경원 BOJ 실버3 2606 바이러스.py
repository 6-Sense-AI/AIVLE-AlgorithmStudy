from collections import deque



## 1번과 연결되어 있으면 무조건 감염

## 그 옆에도 연결되어 있으면 감염

count = -1

def bfs(v):
    global count
    queue = deque([v])
    visited[v] = True
    
    ## 연결된 컴에 있는 거는 다 더함
    while queue:
        com = queue.popleft()
        count += 1
        
        for i in graph[com]:
            if not visited[i]:
                visited[i] = True
                queue.append(i)
    return count



## 컴퓨터 수
n = int(input())  


## 방문상태 초기화
visited = [False]*(n+1)


## 연결 컴퓨터 쌍 수
couple = int(input()) 


## 감염 컴퓨터 수
answer = 0  

## 컴퓨터 연결 상태 초기화
graph = [[] for _ in range(n+1)]   

## 연결 상태 입력
for _ in range(couple):  
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

print(bfs(1))