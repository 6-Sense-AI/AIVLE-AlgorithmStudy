import sys
from collections import deque
input = sys.stdin.readline

n = int(input())    # 정사각형 게임판의 크기
game_map = [list(map(int, input().split())) for _ in range(n)]    # 게임판의 정보

# 이동 가능한 경우
moveX = [1, 0]
moveY = [0, 1]

# 방문 여부 리스트
visited = [[False] * n for _ in range(n)]

def bfs(sx, sy, game_map, visited):
    q = deque([(sx, sy)])    # 큐 선언
    visited[sx][sy] = True

    # 연결된 노드들 모두 꺼내며, 확인
    while q:
        # 현재 위치와 값 저장
        nx, ny = q.popleft()
        now = game_map[nx][ny]

        # 끝점 도달하면, 종료
        if now < 0:
            return True

        # 밟고 있는 값만큼 이동해주기
        for x, y in zip(moveX, moveY):
            dx = nx + x * now
            dy = ny + y * now

            if (0 <= dx < n) and (0 <= dy < n):    # 범위를 넘어가지 않고,
                if not visited[dx][dy]:    # 방문한 적이 없다면,
                    q.append((dx, dy))
                    visited[dx][dy] = True

# 결과 출력
if bfs(0, 0, game_map, visited):
    print("HaruHaru")
else:
    print("Hing")
