import sys
from collections import deque
input = sys.stdin.readline
# 하는중
# 완탐 + bfs
N, M = map(int, input().split()) # 세로, 가로
graph = [list(map(int,input().split())for i in range(N))]

dx = [-1,1,0,0]
dy = [0,0,-1,1]

def bfs(x,y):
    tmp = [] # 테트로미노 배열들
    cnt = 1 # 몇번째 수인지
    q = deque()
    q.append((x,y,cnt))

    while q:
        x, y = q.popleft()

        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]

            if nx < 0 or nx >= N or ny < 0 or ny >= M or nx == 0 and ny == 0:
                continue
            