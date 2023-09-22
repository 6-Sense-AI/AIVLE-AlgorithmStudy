import sys
input = sys.stdin.readline
from collections import deque

# 데큐쓰니 해결.. 허무하도다 !! 허무해 !!

# 톱니 바퀴
t_w = [deque(list(map(int,input().strip()))) for i in range(4)]
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


for _ in range(n):

    start, state = map(int, input().split()) # 시작 num, 회전 방향
    start = start-1 # 인덱스

    # 처음 상태 저장
    temp = [] # 처음 톱니 상태 저장
    for i in range(4):
        temp.append([t_w[i][6], t_w[i][2]])

    # 본인
    # if state == -1 :
    #     tt = re_clock(t_w[start])
    # else : 
    #     clock(t_w[start])     
    t_w[start].rotate(state)


    # 감소
    if start != 0:
        for j in range(start,0,-1):
            if temp[j][0] != temp[j-1][1]:
                if (start-(j-1))%2 == 0:
                    # clock(t_w[j-1]) # 시계
                    t_w[j-1].rotate(state)
                elif (start-(j-1))%2 != 0:
                    # re_clock(t_w[j-1]) # 반시계
                    t_w[j-1].rotate(-1*state)
            elif temp[j][0] == temp[j-1][1]: break
    # 증가
    if start != 3:
        for j in range(start,3):
            if temp[j][1] != temp[j+1][0]:
                if (start-(j+1))%2 == 0:
                    # clock(t_w[j+1]) # 시계
                    t_w[j+1].rotate(state)
                elif (start-(j+1))%2 != 0:
                    # re_clock(t_w[j+1]) # 반시계
                    t_w[j+1].rotate(-1*state)
            elif temp[j][1] == temp[j+1][0]: break   
ans = 0

if t_w[0][0] == 1 : ans+=1
if t_w[1][0] == 1 : ans+=2
if t_w[2][0] == 1 : ans+=4
if t_w[3][0] == 1 : ans+=8

print(ans)