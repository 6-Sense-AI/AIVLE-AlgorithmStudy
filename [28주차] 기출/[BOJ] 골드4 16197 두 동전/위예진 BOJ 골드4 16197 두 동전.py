from collections import deque
import sys
input = sys.stdin.readline

# 입력 받기
r, c = map(int, input().split())    # 세로, 가로의 길이
board = []    # 보드 정보
coins = []    # 코인의 위치
for i in range(r):    # 보드 정보 입력
    tmp = list(input().rstrip())
    board.append(tmp)
    for idx, t in enumerate(tmp):    # 코인 위치 저장
        if t == 'o':
            coins.append([i, idx])
            board[i][idx] = '.'

cnt, ans = 1, -1    # 현재, 최소 이동 횟수
def cal_drop(coins):

    q = deque([[coins, 1]])    # 큐
    while q:
        
        coin, cnt = q.popleft()
        c1, c2 = coin

        # 이동 횟수가 10 넘어가면 종료
        if cnt > 10:
            return -1

        for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            chk = 0    # 둘다 넘어가는지 확인
            moved = []    # 두 코인의 이동 저장

            for coin in [c1, c2]:
                mr, mc = coin[0] + dr, coin[1] + dc

                # 범위를 넘어가지 않으면서,
                if 0 <= mr < r and 0 <= mc < c:
                    # 빈 칸이면 이동
                    if board[mr][mc] == '.':
                        moved.append([mr, mc])
                    # 벽이면, 이동하지 않음
                    else:
                        moved.append([coin[0], coin[1]])
                # 범위를 넘어가면, 동전 떨어짐
                else:
                    chk += 1

            if chk == 1:    # 동전 하나 떨어졌으면, 종료
                return cnt
            elif chk > 1:    # 둘 다 떨어졌으면, 무시
                continue
            else:    # 큐에 추가
                q.append([moved, cnt + 1])

    return -1

print(cal_drop(coins))