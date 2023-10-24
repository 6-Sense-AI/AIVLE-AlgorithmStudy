import sys
input = sys.stdin.readline

N, L = map(int, input().split()) # 신호등 개수, 도로의 길이
now = 0
T = 0 # 이전 위치

for i in range(N):
    D, R, G = map(int, input().split()) # 신호등 위치, 빨, 초
    now += D - T # 현재 위치 - 이전 위치 
    T = 0
    tmp = now
    tmp = tmp % (R+G) # 합을 나누고
    if tmp < R: # 빨간 불이면
        now += R-tmp # 기다림

    T = D # 이전 위치를 빼주기 위해 저장

now += L-T # 도착지 - 마지막 위치
print(now)