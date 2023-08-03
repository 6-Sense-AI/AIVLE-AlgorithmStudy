import sys
from collections import deque
input = sys.stdin.readline

n = int(input())    # 지도의 크기
dt = [list(input().rstrip()) for _ in range(n)]    # 지도의 정보

splt = 0    # 단지수
slist = []    # 각 단지에 속하는 집의 수
visited = [[False] * n for _ in range(n)]    # 방문여부를 나타내는 리스트

# 이동가능한 경로 리스트
mr = [-1, 1, 0, 0]
mc = [0, 0, -1, 1]

# 집의 수를 확인하는 함수
def bfs(dt, sr, sc, visited):
    q = deque([[sr, sc]])    # 큐 선언
    visited[sr][sc] = True    # 방문처리
    house = 1
    global splt

    while q:    # 큐에 갑싱 없어질 때까지 반복
        nr, nc = q.popleft()    # 큐에서 요소 뽑기

        for r, c in zip(mr, mc):    # 이동하기
            mover = nr + r
            movec = nc + c

            if (0 <= mover < n) and (0 <= movec < n):    # 범위를 넘어가지 않고,
                if dt[mover][movec] == '1' and not visited[mover][movec]:    # 집이 있는 곳이고, 방문한 적이 없다면,
                    q.append([mover, movec])    # 큐에 넣고
                    visited[mover][movec] = True    # 방문처리
                    house += 1    # 집의 수 늘려주기

    # 단지 수 늘려주고, 집의 수 저장
    splt += 1
    slist.append(house)    

# 하나씩 단지 확인하기
for r in range(n):
    for c in range(n):
        if not visited[r][c] and dt[r][c] == '1':    # 아직 방문하지 않았으면서, 집이 있는 곳을 만나면
            bfs(dt, r, c, visited)    # 탐색


slist.sort()    # 집의 수 정렬
# 단지 수와 집의 수 출력
print(splt)
for h in slist:
    print(h)