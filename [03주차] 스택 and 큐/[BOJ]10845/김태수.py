from collections import deque
import sys
input = sys.stdin.readline


deq = deque()
n = int(input())
for _ in range(n):
    a = input().strip()
    
    if ' ' in a:
        b, c = a.split()
    else:
        b = a
    
    if b == 'push':
        deq.append(int(c))
    elif b == 'pop':
        if deq:
            print(deq.popleft())
        else:
            print(-1)
    elif b == 'size':
        print(len(deq))
    elif b == 'empty':
        if deq:
            print(0)
        else:
            print(1)
    elif b == 'front':
        if deq:
            print(deq[0])
        else:
            print(-1)
    elif b == 'back':
        if deq:
            print(deq[-1])
        else:
            print(-1)
