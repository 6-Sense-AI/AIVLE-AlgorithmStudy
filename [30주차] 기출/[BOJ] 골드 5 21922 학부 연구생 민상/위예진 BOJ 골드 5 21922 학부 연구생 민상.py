# 시간초과 지옥,,,,
# 왜 함수를 따로 생성해야 더 시간이 적게 걸리지....?

from collections import deque
import sys
input = sys.stdin.readline

rows, cols = map(int, input().split())
airs = deque()    # 에어컨 위치
lab = []    # 연구실 정보
visited = [[0] * cols for _ in range(rows)]    # 원하는 자리 정보
for r in range(rows):
    tmp = list(map(int, input().split()))
    lab.append(tmp)
    for c in range(len(tmp)):
        if tmp[c] == 9:
            airs.append((r, c))
            visited[r][c] = 1

def flow_air(lab, airs):
    # 모든 에어컨을 순회하며 바람 닿는 곳 확인
    while airs:
        ar, ac = airs.popleft()

        # 상, 우, 하, 좌 바람 뻗어나감
        moves = [(-1, 0), (0, 1), (1, 0), (0, -1)]
        for i in range(4):
            dr, dc = moves[i]
            r, c = ar + dr, ac + dc

            while 0 <= r < rows and 0 <= c < cols:
                visited[r][c] = 1    # 자리 체크

                # 에어컨: 종료
                if lab[r][c] == 9: break
                
                if lab[r][c] == 1 and dr == 0:    # ㅣ, (좌/우): 멈춤
                    break
                elif lab[r][c] == 2 and dc == 0:    # ㅡ, (상/하): 멈춤
                    break
                elif lab[r][c] == 3:    # /
                    dr, dc = -dc, -dr
                elif lab[r][c] == 4:    # \
                    dr, dc = dc, dr

                # 이동
                r, c = r + dr, c + dc

    cnt = 0
    for i in visited:
        cnt += i.count(1)

    return cnt

print(flow_air(lab, airs))
# print(sum(sum(visited, [])))    # 이런식으로 계산하면, 시간초과 발생