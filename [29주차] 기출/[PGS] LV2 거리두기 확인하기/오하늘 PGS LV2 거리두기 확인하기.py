from collections import deque

# 시도 1 : 테케는 맞는데 정확도 40%
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
        visited = [[False]*5 for _ in range(5)]
        
        # graph 생성
        for i in range(len(p)):
            g.append(list(p[i]))
        
        flag = 0
        for y in range(5):
            for x in range(5):
                if g[x][y] == 'P':
                    if bfs(x,y,g,visited) == 0 :
                        flag = 1
        if flag == 0: answer.append(1)
        else : answer.append(0)
    
    return answer

places = 	[["POOOP", "OXXOX", "OPXPX", "OOXOX", "POXXP"], ["POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"], ["PXOPX", "OXOXP", "OXPOX", "OXXOP", "PXPOX"], ["OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO"], ["PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"]]

print(solution(places))