from collections import deque

def bfs(p):
    start = []

    for i in range(5):
        for j in range(5):
            if p[i][j] == 'P':
                start.append([i, j])
    for s in start:
        queue = deque([s])
        visited = [[0]*5 for i in range(5)]
        distance = [[0]*5 for i in range(5)]
        visited[s[0]][s[1]] = 1

        while queue:
            y, x = queue.popleft()

            dx = [-1,1,0,0]
            dy = [0,0,-1,1]

            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]

                if 0<=nx<5 and 0<=ny<5 and visited[nx][ny] == 0:
                    
                    if p[ny][nx] == 'O':
                        queue.append([ny,nx])
                        visited[ny][nx] = 1
                        distance[ny][nx] = distance[y][x] + 1

                    if p[ny][nx] == 'P' and distance[y][x] <= 1:
                        return 0
    return 1

    def solution(places):
        answer = []

        for i in places:
            answer.append(bfs(i))

        return answer

# 시도 1 : 테케는 맞는데 정확도 60%
def solution(places):
    answer = []
    
    dx = [-1,1,0,0] # 상하좌우
    dy = [0,0,-1,1]
    
    def bfs (x,y,g,visited) :
        q = deque()
        cnt = 0
        q.append((x,y,cnt))
        
        visited[x][y] = True
        
        while q:
            x,y,cnt = q.popleft()
            cnt+=1
            for i in range(4):
                nx = x+dx[i]
                ny = y+dy[i]
                
                if nx<0 or nx>=5 or ny<0 or ny>=5 or nx==0 and ny==0:
                    continue
                if visited[nx][ny] == 1 :
                    continue
                if cnt == 3 :
                    continue
                if g[nx][ny] == 'X':
                    break
                if g[nx][ny] == 'P':
                    return 0
                visited[nx][ny] = 1
                q.append((nx,ny,cnt))
        return 1
    
    for p in places:
        g = []
        
        # graph 생성
        for i in range(len(p)):
            g.append(list(p[i]))
        
        flag = 0
        for y in range(5):
            for x in range(5):
                visited = [[False]*5 for _ in range(5)]
                if g[x][y] == 'P':
                    if bfs(x,y,g,visited) == 0 :
                        flag = 1
        if flag == 0: answer.append(1)
        else : answer.append(0)
    
    return answer

places = [["POOPO", "OOOOO", "OOOXP", "OPOPX", "OOOOO"]]

print(solution(places))