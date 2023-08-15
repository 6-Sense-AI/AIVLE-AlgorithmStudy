# 1차시도 : 시간초과
# visited 함수 추가
# 2차시도 : 시간초과
# if arr[x][y] == 0: break 추가
# 3차시도 : 해결!

import sys
input = sys.stdin.readline
from collections import deque

n = int(input())
visited = [[False]*n for _ in range(n)]

arr = []
for i in range(n):
    arr.append(list(map(int, input().split())))

def bfs(x, y, arr):
    q = deque()
    q.append((x,y))

    while q:
        x,y = q.popleft()
        
        if arr[x][y] == 0: # 이 조건문을 넣지 않으면 무한루프 가능성이 있음
            break
        
        for i in range(2):
            if i == 0 : # 아래
                if x+int(arr[x][y]) < 0 or x+int(arr[x][y])>=n:
                    continue
                if arr[x+int(arr[x][y])][y] == -1:
                    print("HaruHaru")
                    return
                if not visited[x+int(arr[x][y])][y]:
                    q.append((x+int(arr[x][y]),y))
                    visited[x+int(arr[x][y])][y] == True
            if i == 1 : # 오른쪽
                if y+int(arr[x][y]) < 0 or y+int(arr[x][y]) >=n:
                    continue
                if arr[x][y+int(arr[x][y])] == -1:
                    print("HaruHaru")
                    return
                if not visited[x][y+int(arr[x][y])]:
                    q.append((x,y+int(arr[x][y])))
                    visited[x][y+int(arr[x][y])] == True

    print('Hing')

bfs(0,0,arr)
