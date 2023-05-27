# 프로그래머스 : 게임 맵 최단거리
from collections import deque

def solution(maps):
    answer = -1
    
    dx = [-1, 1, 0, 0] # 상, 하, 좌, 우
    dy = [0, 0, -1, 1]
    
    def bfs(x,y): # 시작 좌표
        q = deque()
        q.append((x, y))
        
        while q:
            x, y = q.popleft()
            
            for i in range(4):    
                nx = x+dx[i]
                ny = y+dy[i]
                
                if nx < 0 or nx >= len(maps) or ny < 0 or ny >= len(maps[0]) or nx ==0 and ny == 0:
                    continue
                if maps[nx][ny] == 0:
                    continue
                if maps[nx][ny] == 1:
                    maps[nx][ny] = maps[x][y]+1
                    q.append((nx, ny))
                    
        return maps[len(maps)-1][len(maps[0])-1]
    
    answer = bfs(0,0)
    if answer == 1: return -1
    return answer
