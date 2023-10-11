import sys
input = sys.stdin.readline

rows, cols = map(int, input().split())
grid = list(list(map(int, input().split())) for _ in range(rows))

# 이동가능한 방법 (상, 하, 좌, 우)
moves = [(-1, 0), (1, 0), (0, -1), (0, 1)]
# 방문여부 확인 리스트
visited = [[False] * cols for _ in range(rows)]
res = 0    # 최대합

# 테트리스 하나를 놓는 함수 (ㅏ 모양 제외)
def make_tetris(cnt, now_sum, now):
    global res

    # 종료 조건
    if cnt >= 4:
        res = max(res, now_sum)
        return
        
    for mr, mc in moves:
        nowR, nowC = now[0] + mr, now[1] + mc
        if 0 <= nowR < rows and 0 <= nowC < cols:
            if not visited[nowR][nowC]:
                visited[nowR][nowC] = True
                make_tetris(cnt + 1, now_sum + grid[nowR][nowC], (nowR, nowC))
                visited[nowR][nowC] = False

# ㅗ ㅜ ㅏ ㅓ 만 고려했을 때, 최대합 계산            
def make_tetirs_rest(r, c):
    global res

    for n in range(4):
        # 초기값은 시작지점의 값으로 지정
        tmp = grid[r][c]
        for k in range(3):
            # moves 배열의 요소를 3개씩 사용할 수 있도록 인덱스 계산
            # 012, 123, 230, 301
            t = (n + k) % 4
            ni = r + moves[t][0]
            nj = c + moves[t][1]

            if not (0 <= ni < rows and 0 <= nj < cols):
                tmp = 0
                break
            tmp += grid[ni][nj]
        # 최대값 계산
        res = max(res, tmp)

# 테트리스 계산 시작
for r in range(rows):
    for c in range(cols):
        visited[r][c] = True
        make_tetris(1, grid[r][c], (r, c))
        visited[r][c] = False

        make_tetirs_rest(r, c)
print(res)