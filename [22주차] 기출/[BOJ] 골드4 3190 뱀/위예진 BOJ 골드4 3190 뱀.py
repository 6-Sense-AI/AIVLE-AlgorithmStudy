from collections import deque
import sys
input = sys.stdin.readline

# 입력 받기
n = int(input())    # 보드의 크기
board = list([0] * n for _ in range(n))    # 보드 (빈 곳: 0, 뱀: 1, 사과: 2)
num_a = int(input())    # 사과의 개수
for _ in range(num_a):    # 사과의 위치
    r, c = map(int, input().split())
    board[r-1][c-1] = 2
num_dir = int(input())    # 뱀의 방향 변환 횟수
rotations = list((input().split()) for _ in range(num_dir))    # 뱀의 방향 변환 정보 (숫자 x, 문자 c)

# 초기 설정
dir = [(0, 1), (1, 0), (0, -1), (-1, 0)]    # 우, 하, 좌, 상
snake = deque([(0, 0)])    # 뱀의 위치 리스트 (꼬리, ..., 몸통, ..., 머리)
board[0][0] = 1    # 첫째칸에 뱀 위치
dir_idx = 0    # 현재 바라보는 방향
now = 0    # 현재 시간

# 이동 함수
def move_snake(t):
    global dir_idx, now

    # 시간 초만큼 이동
    while now < t:
        now += 1    # 현재 시간 변경
        
        # 한 칸 이동
        moveR = snake[-1][0] + dir[dir_idx][0]
        moveC = snake[-1][1] + dir[dir_idx][1]

        # 벽에 부딪히면, 종료
        if moveR < 0 or moveR >= n or moveC < 0 or moveC >= n:    
            return False
        
        # 빈 곳이면, 머리 위치시키고 꼬리 이동
        if board[moveR][moveC] == 0:
            # 머리 위치시킴
            snake.append((moveR, moveC))
            board[moveR][moveC] = 1
            # 꼬리 이동
            xr, xc = snake.popleft()
            board[xr][xc] = 0
        # 자기자신의 몸과 부딪히면, 종료
        elif board[moveR][moveC] == 1:
            return False
        # 사과가 위치한다면, 머리만 늘려주기
        elif board[moveR][moveC] == 2:
            snake.append((moveR, moveC))
            board[moveR][moveC] = 1

    return True

check = True    # 종료조건 도달 여부 확인
for x, c in rotations:
    check = move_snake(int(x))
    if not check:    # 종료조건 도달하면, 종료
        break
            
    # 방향 변환
    if c == 'L':    # 왼쪽으로 90도
        dir_idx = (dir_idx + 3) % 4
    elif c == 'D':      # 오른쪽으로 90도
        dir_idx = (dir_idx + 1) % 4

# 방향 변환 끝난 이후에도 이동
while check:
    check = move_snake(now + 1)

print(now)