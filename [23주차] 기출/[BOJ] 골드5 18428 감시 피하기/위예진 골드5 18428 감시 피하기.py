# 학생이 있다면 S, 선생님이 있다면 T, 아무것도 존재하지 않는다면 X
# 복도의 빈 칸 중에서 장애물을 설치할 위치를 골라, 정확히 3개의 장애물을 설치
# 3개의 장애물을 설치하여 모든 학생들을 감시로부터 피하도록 할 수 있는지 계산

import sys
input = sys.stdin.readline

# 모든 학생들이 감시를 피하는지 확인하는 함수
def check_run():

    # 감시 가능한 방향 (상하좌우)
    dir = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    # 모든 선생님들이 학생과 마주치는지 확인
    for tr, tc in teachers:
        for dr, dc in dir:    # 상하좌우 확인
            nowR, nowC = tr, tc

            while 0 <= nowR < n and 0 <= nowC < n:
                # 장애물 있으면, 반복 종료
                if hall[nowR][nowC] == 'O':
                    break
                # 학생과 마주치면, False 반환
                if hall[nowR][nowC] == 'S':
                    return False
                
                nowR += dr
                nowC += dc

    # 학생과 마주친 적 없이 종료되면, True 반환       
    return True

# 장애물을 설치하는 함수
def set_obj(cnt):
    global ans

    # 종료조건 확인
    if cnt == 3:
        if check_run():
            ans = 'YES'
            return
    else:
        for r in range(n):
            for c in range(n):
                if hall[r][c] == 'X':
                    hall[r][c] = 'O'
                    set_obj(cnt + 1)
                    hall[r][c] = 'X'
                
# 메인 시작
n = int(input())    # 복도의 크기
hall = []    # 복도 정보
teachers = []    # 선생님의 위치 리스트
for i in range(n):
    hall.append(list(input().split()))
    for j in range(n):
        if hall[i][j] == 'T':    # 선생님 위치 입력받음
            teachers.append((i, j))

ans = 'NO'
set_obj(0)
print(ans)