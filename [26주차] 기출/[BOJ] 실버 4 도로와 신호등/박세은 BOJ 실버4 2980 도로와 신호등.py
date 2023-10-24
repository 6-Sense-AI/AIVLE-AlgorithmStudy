# 나만 왤캐 원시인처럼 풀었지..? 다들 천재임?

import sys
import copy

input = sys.stdin.readline

n, l = map(int, input().split())

state = [True for _ in range(l+1)] # 도로 상태 : False -> 빨간불, True -> 파란불 or 일반도로
tl = [] # 신호등 정보 [D, R, G]

for _ in range(n):
    # D = 신호등 위치, 
    # R = 빨간색 지속 시간, 
    # G = 초록색 지속 시간 순
    t = list(map(int, input().split()))

    tl.append(t)

    state[t[0]] = False # 신호등은 빨간불로 시작하므로, 신호등 위치 False

tl_cpy = copy.deepcopy(tl) # 신호등은 무한히 작동하므로, 원본값을 따로 저장해둔다.

# 신호등 카운트
def tl_cnt():
    # 모든 신호등 카운트가 한번에 바뀌어야 하므로 for문 돌며 값 바꿔주기
    for i in range(len(tl_cpy)):
        if tl_cpy[i][1] > 0: # 아직 빨간불이 지속중이면, (0이 아니면)
            state[tl_cpy[i][0]] = False # 도로 상태 False
            tl_cpy[i][1] -= 1 # 빨간불 카운트 차감

            if tl_cpy[i][1] == 0: # 0이 되는 순간, 초록불이 활성화 돼야 하므로 if문 추가
                state[tl_cpy[i][0]] = True # 0이 되면 True
        
        elif tl_cpy[i][1] == 0 and tl_cpy[i][2] > 0: # 빨간불 카운트를 모두 소진했으며, 초록불 카운트가 유효하면
            state[tl_cpy[i][0]] = True # 초록불 활성화
            tl_cpy[i][2] -= 1 # 초록불 카운트 차감

            if tl_cpy[i][2] == 0: # 초록불이 0이 되는 순간, 빨간불 활성화와 동시에 신호등 카운트 초기화를 위해 if문 추가
                state[tl_cpy[i][0]] = False 
                # 신호등 카운트 초기화
                tl_cpy[i][1] = tl[i][1]
                tl_cpy[i][2] = tl[i][2]

time = 0 # 지속 시간 (답)
mv = 0 # 현재 위치

while mv < l: # 끝에 도달할 때 까지 반복
    
    if state[mv]: # 현 위치가 True 라면
        
        tl_cnt()

        time += 1 # 소요 시간 +
        mv += 1 # True인 상태이므로, 다음 칸으로 이동
    
    else: # 현 위치가 False라면

        tl_cnt()
  
        time += 1 # 소요 시간만 +

print(time)

    







