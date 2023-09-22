import sys
input = sys.stdin.readline

# 구글 안보고 1차 시도

# 톱니 바퀴
t_w = [list(map(int,input().strip())) for i in range(4)]
# 1번은 idx 2, 2번은 26, 3번도 26 4번은 6 -> 맞닿은 곳

# 회전 횟수
n = int(input())

def clock(arr): # 시계
    cl_temp = arr[7]
    for i in range(7,0,-1):
        arr[i] = arr[i-1]
    arr[0] = cl_temp
    
def re_clock(arr): # 반시계
    cl_temp = arr[0]
    for i in range(7):
        arr[i] = arr[i+1]
    arr[7] = cl_temp


for i in range(n):

    start, state = map(int, input().split()) # 시작 num, 회전 방향
    # 1 시계  -1 반시계

    # 처음 상태 저장
    temp = [] # 처음 톱니 상태 저장
    for j in range(4):
        temp.append([t_w[j][6], t_w[j][2]])

    # 본인
    if state == -1 :
        tt = re_clock(t_w[start-1])
    else : 
        clock(t_w[start-1])

    # 감소
    i = 0
    while 1: 
        if start - i < 2: break # 감소 다 시켰으면 나옴

        if temp[start-i-1][0] == temp[start-i-2][1]: break # 현재와 이전 값 비교

        else :
            state = -state
            if state == -1 :
                re_clock(t_w[start-1])
            else : 
                clock(t_w[start-1])
            i -= 1

    i = 0
    # # 증가
    while 1: 
        if start + i > 3: break # 감소 다 시켰으면 나옴

        if temp[start+i-1][1] == temp[start+i][0]: break # 현재와 다음 값 비교

        else :
            state = -state
            if state == -1 :
                tt = re_clock(t_w[start])
            else : 
                clock(t_w[start])
            i += 1
    print(t_w)

print(t_w)

ans = 0

if t_w[0][0] == 1 : ans+=1
if t_w[1][0] == 1 : ans+=2
if t_w[2][0] == 1 : ans+=4
if t_w[3][0] == 1 : ans+=8

print(ans)