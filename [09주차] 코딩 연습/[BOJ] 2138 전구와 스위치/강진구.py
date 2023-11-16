# 나는 바보예요~ 워~

import sys

input = sys.stdin.readline

n = int(input())

swich = list(input().strip())
goal = list(input().strip())

def change(i,lst):
    for j in [i-1,i,i+1]:
        if 0<=j<n:
            if lst[j] == '1':
                lst[j] = '0'
            else:
                lst[j] = '1'
    return lst

cnt = 0

while swich != goal:
    for i in range(n):
        if swich[i] != goal[i]:
            swich = change(i,swich)
            cnt += 1

print(cnt)
