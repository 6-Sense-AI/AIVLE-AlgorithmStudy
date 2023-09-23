import sys
input = sys.stdin.readline

from collections import deque # 데큐

# 뱀 - 해결
# Dummy라는 도스 게임
# 답 = 몇초에 끝나는지

# 시간 오래걸린 부분
# 문제 이해를 잘못함 회전 조건에서 8, D -> 10, D 일때
# 8초 뒤에 10초 뒤에.. 가 아니라 8초에서 회전 10초에서 회전이므로 10-8 이렇게 해서 풀어야 했음.

n = int(input()) # 보드의 크기
arr = [[0] *n for i in range (n)]
k = int(input()) # 사과의 개수

for _ in range(k): # 사과 정보
    row, col = map(int,input().split())
    arr[row-1][col-1] = 1

s_info = [] # 뱀 정보
l = int(input()) # 방향 변환 횟수
temp = 0
for _ in range(l):
    sec, d = input().split()
    sec = int(sec) - temp
    s_info.append((int(sec),d))
    temp = temp + sec

#게임 시작 시간으로부터 sec초가 끝난 뒤에 왼쪽(C가 'L') 또는 오른쪽(C가 'D')로 90도 방향을 회전시킨다는 뜻이다. X는 10,000 이하의 양의 정수이며, 방향 전환 정보는 X가 증가하는 순으로 주어진다.

dx = [0,1,0,-1] # 우하좌상 (시계방향)
dy = [1,0,-1,0]
d = 0 # 이게 뭐냐면 방향 지정이랍니다.

q = deque() 
q.append((0,0)) # start


# 게임 시작
cnt = 0
flag = 0
i = 0
while 1:
    apple = 0 # 사과 초기화
    sss, ddd = s_info[i] # 시간과, 방향

    j = 0
    while 1 : # 초
        x,y = q[-1] # 가장 마지막에 넣은 머리 좌표

        # 전진
        nx = x + dx[d]
        ny = y + dy[d]

        if 0 > nx or nx >= n or ny <0 or ny >= n: 
            flag = 1
            break # 벽에 부딪힘

        for ii in q :
            if ii == (nx,ny):
                flag = 1
                break # 본인임
        if flag == 1 : break

        q.append((nx,ny)) #머리 진출

        # 사과가 있으면
        if arr[nx][ny] == 1 :
            arr[nx][ny] = 0 #사과 먹음
        else : q.popleft() # 꼬리 자름

        cnt += 1
        # n초 후 방향 전환
        if j == sss-1:
            if ddd == 'L' : # 방향이 왼쪽
                d = (d+3)%4 # 왼쪽으로 회전
            else : # 방향 오른쪽
                d = (d+1)%4 #오른쪽으로 회전
            
            i+=1
            if i < l : 
                break
            else : j += 1

        else :
            j += 1
    
    if flag == 1: break

print(cnt+1)