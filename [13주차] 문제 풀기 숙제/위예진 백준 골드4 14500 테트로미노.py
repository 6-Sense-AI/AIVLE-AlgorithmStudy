# 종이의 범위를 넘지 않으면서, 연속적인 칸 4개를 방문하면 됨.
# but, ㅏㅗㅜㅓ 모양은 다시 돌아가서 방문해야 함 (-> 이를 고려해줘야 함)

import sys
from itertools import combinations
input = sys.stdin.readline

row, col = map(int, input().split())
note = [list(map(int, input().split())) for _ in range(row)]

move = [(1, 0), (-1, 0), (0, 1), (0, -1)]    # 이동 가능한 경우의 수 (상하좌우)
res = 0    # 최대합
visited = [[False] * col for _ in range(row)]

# ㅗ ㅜ ㅏ ㅓ 제외했을 때, 최대합 계산
def search_note(r, c, cur, cnt): 
    global res
    if cnt == 4:    # 4칸을 다 방문했을 때
        res = max(cur, res)    # 현재까지의 합과 기존 값 중 큰 값으로 결과 변경
        return
    
    for i, j in move:
        mr = r + i
        mc = c + j
        
        if 0 <= mr < row and 0 <= mc < col:    # 이동한 곳이 범위를 넘어가지 않고, 
            if not visited[mr][mc]:    # 방문한 적이 없다면
                # 방문 표시 및 순회 후, 다시 표시 제거
                visited[mr][mc] = True
                search_note(mr, mc, cur + note[mr][mc], cnt + 1)
                visited[mr][mc] = False
    
# ㅗ ㅜ ㅏ ㅓ 만 고려했을 때, 최대합 계산            
def search_note_rest(r, c):
    global res
    for n in range(4):
        # 초기값은 시작지점의 값으로 지정
        tmp = note[r][c]
        for k in range(3):
            # move 배열의 요소를 3개씩 사용할 수 있도록 인덱스 계산
            # 012, 123, 230, 301
            t = (n+k)%4
            ni = r+move[t][0]
            nj = c+move[t][1]

            if not (0 <= ni < row and 0 <= nj < col):
                tmp = 0
                break
            tmp += note[ni][nj]
        # 최대값 계산
        res = max(res, tmp)
    
    # global res
    
    # for combi in combinations(move, 3):    # 3개를 고른, 4가지 경우의 수 모두 고려
    #     now = note[r][c]    # 현재 최대값을 처음 위치로 지정함
        
    #     for i, j in combi:
    #         mr = r + i
    #         mc = c + j
            
    #         if not (0 <= mr < row and 0 <= mc < col):    # 범위를 넘어간다면, 해당 경우의 수 버리기
    #             now = 0
    #             break
            
    #         now += note[mr][mc]
            
    res = max(res, now)    # 최대값으로 갱신하기
        
    
                
for r in range(row):
    for c in range(col):
        visited[r][c] = True    # 시작점 방문처리
        search_note(r, c, note[r][c], 1)
        visited[r][c] = False    # 시작점 방문처리 해제
        
        search_note_rest(r, c)
        
print(res)