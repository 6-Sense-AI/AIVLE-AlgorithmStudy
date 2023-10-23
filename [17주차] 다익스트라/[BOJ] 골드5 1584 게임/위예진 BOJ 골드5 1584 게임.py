# 잃는 생명의 최소값 -> 0-1 bfs
# => 가중치 생기는 건 뒤쪽으로, 안생기는 건 앞쪽으로! 넣어주고 앞부터 탐색
from collections import deque

N = 501    # 구역의 한 변의 크기
area = [[0] * N for _ in range(N)]    # 구역의 정보

# 위험한 구역은 1로 가중치 설정
w = int(input())    
for _ in range(w):
    wx1, wy1, wx2, wy2 = map(int, input().split())
    for r in range(min(wx1, wx2), max(wx1, wx2) + 1):
        for c in range(min(wy1, wy2), max(wy1, wy2) + 1):
            area[r][c] = 1
# 죽음의 구역은 -1로 가중치 설정
d = int(input())    
for _ in range(d):
    wx1, wy1, wx2, wy2 = map(int, input().split())
    for r in range(min(wx1, wx2), max(wx1, wx2) + 1):
        for c in range(min(wy1, wy2), max(wy1, wy2) + 1):
            area[r][c] = -1

q = deque([(0, 0, 0)])    # row, col, life
visited = [[False] * N for _ in range(N)]    # 방문여부
chk = True

while q:
    nr, nc, life = q.popleft()

    # 목표 위치 도달 확인
    if (nr, nc) == (N - 1, N - 1):
        chk = False
        ans = life
        break

    for rr, cc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        mr, mc = nr + rr, nc + cc

        # 범위를 넘어가거나, 죽음의 지역일 때, 방문한 적 있을 때, 넘기기
        if mr < 0 or mr >= N or mc < 0 or mc >= N: 
            continue
        if area[mr][mc] < 0 :
            continue
        if visited[mr][mc]:
            continue
        
        # 방문여부 처리
        visited[mr][mc] = True

        # 가중치 계산해서 넣어주기
        if area[mr][mc]:    # 위험 지역: 뒤에 넣기
            q.append((mr, mc, life + 1))
            # 위험지역 -> 위험지역
        else:    # 안전 지역: 앞에 넣기
            q.appendleft((mr, mc, life))
            
if chk:
    print(-1)
else:
    print(ans)