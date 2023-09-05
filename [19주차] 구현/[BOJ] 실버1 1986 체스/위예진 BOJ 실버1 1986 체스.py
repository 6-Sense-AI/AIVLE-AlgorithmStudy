# Queen: 가로, 세로, 대각선 무제한 이동 가능. 장애물 있을 시, 이동 불가
# Knight: 2x3 직사각형에서 반대쪽 꼭짓점으로 이동 가능. 장애물 있을 시, 이동 가능
# Pawn: 장애물 역할만 함
# 안전한 칸이 몇 칸인지 출력

import sys
input = sys.stdin.readline

rows, cols = map(int, input().split())    # 체스판의 크기
chess = [[False] * cols for _ in range(rows)]    # 각 체스판의 정보
safe = [[1] * cols for _ in range(rows)]    # 안전한 칸 1로 초기화

# 체스판 정보 채우기
for name in ['Q', 'K', 'P']:
    tmp = list(map(int, input().split()))
    for j in range(1, tmp[0] * 2 + 1, 2):
        chess[tmp[j]-1][tmp[j+1]-1] = name

# Queen과 Knight의 이동가능한 경로
qmove = [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (1, -1), (1, 1), (-1, 1)]
kmove = [(-1, -2) , (-2, -1), (1, -2), (2, -1), (1, 2), (2, 1), (-1, 2), (-2, 1)]

# 하나씩 안전하지 않은 칸 확인하기 (0으로 채움)
for r in range(rows):
    for c in range(cols):

        # Queen일 때
        if chess[r][c] =='Q':    
            safe[r][c] = 0    # Queen 위치는 모두 안전 X
            # 이동가능한 모든 곳을 안전하지 않은 칸으로 설정
            for mr, mc in qmove:
                for i in range(1, max(rows, cols)):
                    moveR = r + mr * i
                    moveC = c + mc * i
                    
                    if 0 <= moveR < rows and 0 <= moveC < cols:    # 범위를 넘지 않으면
                        if chess[moveR][moveC]:    # 장애물 있으면 멈춤
                            break
                        safe[moveR][moveC] = 0
        # Knight일 때
        elif chess[r][c] =='K':    # Knight일 때
            safe[r][c] = 0    # Queen 위치는 모두 안전 X
            # 이동가능한 모든 곳을 안전하지 않은 칸으로 설정
            for mr, mc in kmove:
                moveR = r + mr
                moveC = c + mc
                if 0 <= moveR < rows and 0 <= moveC < cols:
                    safe[moveR][moveC] = 0
        # Pawn일 때
        elif chess[r][c] =='P':    
            # Pawn 위치는 모두 안전하지 않은 칸으로 설정
            safe[r][c] = 0

print(sum(sum(safe, [])))



################################################################################# 시간 초과난 방식
# 말들의 위치들만 저장해서 Queen 순회 시, 장애물 있는지 확인할 때의 시간복잡도가 컸음


# # Queen: 가로, 세로, 대각선 무제한 이동 가능. 장애물 있을 시, 이동 불가
# # Knight: 2x3 직사각형에서 반대쪽 꼭짓점으로 이동 가능. 장애물 있을 시, 이동 가능
# # Pawn: 장애물 역할만 함
# # 안전한 칸이 몇 칸인지 출력

# import sys
# input = sys.stdin.readline

# rows, cols = map(int, input().split())    # 체스판의 크기
# chess = {'Queen': [], 'Knight': [], 'Pawn': []}    # 각 체스판의 위치
# safe = [[1] * (cols) for _ in range(rows)]    # 안전한 칸 1로 초기화

# # 위치 입력 받기
# for name in chess.keys():
#     tmp = list(map(int, input().split()))
#     # chess[name].append(tmp[0])
#     for j in range(1, tmp[0] * 2 + 1, 2):
#         chess[name].append((tmp[j], tmp[j+1]))

# # Queen과 Knight의 이동가능한 경로
# qmove = [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (1, -1), (1, 1), (-1, 1)]
# kmove = [(-1, -2) , (-2, -1), (1, -2), (2, -1), (1, 2), (2, 1), (-1, 2), (-2, 1)]

# # 하나씩 안전하지 않은 칸 확인하기 (0으로 채움)
# for name in chess.keys():

#     if name == 'Queen':    # Queen일 때
#         # Queen이 존재하는 모든 칸 순회
#         for r, c in chess.get(name):
#             safe[r-1][c-1] = 0    # Queen 위치는 모두 안전 X
#              # 이동가능한 모든 곳을 안전하지 않은 칸으로 설정
#             for mr, mc in qmove:
#                 for i in range(1, max(rows, cols)):
#                     moveR = r-1 + mr * i
#                     moveC = c-1 + mc * i
                    
#                     if (moveR+1, moveC+1) in sum(list(chess.values()), []):    # 장애물 있으면 멈춤
#                         break
#                     if 0 <= moveR < rows and 0 <= moveC < cols:
#                         safe[moveR][moveC] = 0
#     elif name == 'Knight':    # Knight일 때
#         # Knight가 존재하는 모든 칸 순회
#         for r, c in chess.get(name):
#             safe[r-1][c-1] = 0    # Knight 위치는 모두 안전 X
#             # 이동가능한 모든 곳을 안전하지 않은 칸으로 설정
#             for mr, mc in kmove:
#                 moveR = r-1 + mr
#                 moveC = c-1 + mc
#                 if 0 <= moveR < rows and 0 <= moveC < cols:
#                     safe[moveR][moveC] = 0
#     else:    # Pawn일 때
#         # Pawn 위치는 모두 안전하지 않은 칸으로 설정
#         for r, c in chess.get(name):
#             safe[r-1][c-1] = 0

# print(sum(sum(safe, [])))