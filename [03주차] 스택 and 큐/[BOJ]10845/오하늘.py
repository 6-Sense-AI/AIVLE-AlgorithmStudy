import sys
input = sys.stdin.readline
from collections import deque

n = int(input())
deq = deque()

for i in range(0,n):
    r = input()
    if r.startswith('pu'): #push
        str = r.split()
        deq.append(str[1])
    elif r.startswith('pop'): #pop
        if len(deq) == 0: print(-1)
        else : print(deq.popleft()) # 맨 앞
    elif r.startswith('s'): #size
        print(len(deq))
    elif r.startswith('em'): #empty
        if len(deq) == 0: print(1)
        else : print(0)
    elif r.startswith('f'): #front
        if len(deq) == 0:  print(-1)
        else :
            a = deq.popleft()
            print(a)
            deq.appendleft(a) # 다시 추가
    elif r.startswith('b'): #back
        if len(deq) == 0:
            print(-1)
        else :
            a = deq.pop()
            print(a)
            deq.append(a) # 다시 추가
