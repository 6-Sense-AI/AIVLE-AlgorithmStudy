
## 죽음의 구역 못 들어감

## 위험한 구역은 1회 이동당 생명력 -1

## 나머지는 안전한 구역

## 생명력 최소로 잃는 프로그램

## 다익보다 데큐 느낌?

import sys
from collections import deque
input = sys.stdin.readline

## 게임존 초기화

graph = [[0 for _ in range(501)] for _ in range(501)]


## 위험구역 1로 표시
## x와 y 순서 정렬을 최대최소로 한다

N = int(input())  
for _ in range(N):
    x1, y1, x2, y2 = map(int, input().rstrip().split())
    for row in range(min(x1, x2), max(x1, x2)+1):
        for col in range(min(y1, y2), max(y1, y2)+1):
            graph[row][col] = 1  

## 죽음구역 2로 표시
M = int(input())
for _ in range(M):
    x1, y1, x2, y2 = map(int, input().rstrip().split())
    for row in range(min(x1, x2), max(x1, x2)+1):
        for col in range(min(y1, y2), max(y1, y2)+1):
            graph[row][col] = 2  



queue = deque()
queue.append((0, 0, 0))  # row, col, time
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]
while queue:
    row, col, time = queue.popleft()
    if (row, col) == (500, 500):
        print(time)
        break
    else:
        for i in range(4):
            now_row, now_col = row+dr[i], col+dc[i]
            if now_row > 500 or now_row < 0 or now_col > 500 or now_col < 0:
                continue


            ## 생명력 안 깎이면 왼쪽 삽입
            if graph[now_row][now_col] == 0:
                graph[now_row][now_col] = 2
                queue.appendleft((now_row, now_col, time))
            
            ## 깎이면 오른쪽 삽입
            elif graph[now_row][now_col] == 1:
                graph[now_row][now_col] = 2
                queue.append((now_row, now_col, time+1))
else:
    print(-1)