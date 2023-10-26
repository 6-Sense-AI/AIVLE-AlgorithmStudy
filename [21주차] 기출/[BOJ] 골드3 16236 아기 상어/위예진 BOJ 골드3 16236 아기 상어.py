# 제일 어려워써여,,,,,,,,고통,,,,

from collections import deque
import sys
input = sys.stdin.readline

n = int(input())    # 공간의 크기
graph = []    # 공간의 상태
for i in range(n):
    tmp = list(map(int, input().split()))
    graph.append(tmp)

    if 9 in tmp:    # 아기 상어의 위치 저장
        nowR, nowC = i, tmp.index(9)    # 아기 상어의 현재 위치

move = [(-1, 0), (0, -1), (1, 0), (0, 1)]    # 상, 좌, 하, 우
now_size, now_eat = 2, 0    # 현재 크기, 먹은 먹이
sec = 0    # 지난 시간

# 가장 가까운 거리의 먹이 위치 찾는 함수
def eat_fishes(row, col):    
    visited = [[0] * n for _ in range(n)]    # 방문 여부 리스트(이동 횟수도 표시)
    cand = []    # 이동 위치 후보들

    # 첫 시작위치 방문처리
    visited[row][col] = 1
    q = deque([(row, col)])

    while q:
        r, c = q.popleft()

        for dr, dc in move:
            mr = r + dr
            mc = c + dc

            # 범위 및 방문 여부 확인
            if mr < 0 or mr >= n or mc < 0 or mc >= n:
                continue
            if visited[mr][mc]:
                continue

            # 먹이 먹을 수 있으면, 후보 리스트에 넣어주기
            if 0 < graph[mr][mc] < now_size:
                # 시작 위치 방문처리하며 1을 더해줬으므로, 실제 step보다 1 큰 것 고려
                cand.append([visited[r][c], mr, mc])
                visited[mr][mc] = visited[r][c] + 1
            # 현재 크기와 같거나 빈칸이면, 이동 큐에 넣어주기
            elif graph[mr][mc] == now_size or graph[mr][mc] == 0:
                q.append((mr, mc))
                visited[mr][mc] = visited[r][c] + 1

    # 우선 조건대로 정렬 (거리, 상, 좌)             
    cand = sorted(cand, key=lambda x: (x[0], x[1], x[2]))

    # 첫 번째 요소만 출력(없으면 빈 리스트 출력)
    return cand[:1]

# 더이상 먹을 먹이가 없을 때까지 순회
while True:
    nxt = eat_fishes(nowR, nowC)

    # 종료 조건
    if not nxt:
        break
    
    # 이동
    step, r, c = nxt.pop()
    graph[nowR][nowC] = 0
    nowR, nowC = r, c
    # 먹기
    sec += step
    now_eat += 1

    # 먹은 먹이 확인, 사이즈 키우기
    if now_eat == now_size:
        now_size += 1
        now_eat = 0    # 먹은 먹이 초기화

print(sec)