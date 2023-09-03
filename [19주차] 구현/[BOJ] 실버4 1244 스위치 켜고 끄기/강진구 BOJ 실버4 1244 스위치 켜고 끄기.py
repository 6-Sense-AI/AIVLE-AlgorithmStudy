# 남학생 배수, 여학생 받은 거 중심 같은거 최대로 

import sys
from collections import deque

input = sys.stdin.readline

num = int(input())

switch = list(map(int, input().split()))

st_num = int(input())

student = [list(map(int, input().split())) for _ in range(st_num)]

que = deque(student)

def change(sw):
    if sw == 1:
        sw = 0
    else:
        sw = 1
    return sw

while que:
    sex, idx = que.popleft()
    if sex == 1:
        for i in range(1,100):
            if idx*i - 1 < num:
                switch[(idx*i)-1] = change(switch[(idx*i)-1])
            else:
                break
    else:
        switch[idx-1] = change(switch[idx-1])
        for i in range(1,100):
            if 0<=idx-1-i and idx-1+i<num:
                if switch[idx-1-i] == switch[idx-1+i]:
                    switch[idx-1-i] = change(switch[idx-1-i])
                    switch[idx-1+i] = change(switch[idx-1+i])
                else:
                    break
            else:
                break

for i,s in enumerate(switch):
    print(s, end = ' ')
    if (i+1)//20 == (i+1)/20:
        print()