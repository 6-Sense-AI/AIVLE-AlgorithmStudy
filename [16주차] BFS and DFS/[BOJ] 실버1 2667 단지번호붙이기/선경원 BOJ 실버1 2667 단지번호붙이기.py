from collections import deque

## 첫 번째 줄에는 지도의 크기 N 입력

n = int(input())

## 지도 입력

housing =  [list(input().rstrip()) for _ in range(n)] 

#print(housing)
           
## 연결되었다는 것은 어떤 집이 좌우, 혹은 아래위로 다른 집이 있는 경우

## 현재 위치가 1이고 상하좌우 중 한 방향으로 이동했을 경우 1이면 단지

## 단지별로 집 수를 계산해서 리스트에 넣은 다음 집 수 초기화

## 상하좌우 이동

dx = [0,0,1,-1]
dy = [1,-1,0,0]

visited = [[False]*n for _ in range(n)]

## 단지 수와 단지별 집 수 리스트 초기화

Danji = 0
Danji_house = []

# print(visited)

def bfs(housing, a, b, visited):
    queue = deque([(a,b)])    
    visited[a][b] = True

    global Danji

    ## 집은 최소 1개부터 시작
    cnt = 1

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]

            if 0<=nx<n and 0<=ny<n:
                if housing[nx][ny] == '1' and not visited[nx][ny]:
                    queue.append([nx,ny])
                    visited[nx][ny] = True
                    cnt+=1
    Danji+=1
    Danji_house.append(cnt)


for xx in range(n):
    for yy in range(n):
        if not visited[xx][yy] and housing[xx][yy] == '1':  
            bfs(housing, xx, yy, visited)    

Danji_house.sort()

print(Danji)

for i in Danji_house:
    print(i)
