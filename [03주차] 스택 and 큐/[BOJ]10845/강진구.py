import sys
from collections import deque

input = sys.stdin.readline

n = int(input())
que = deque()

for _ in range(n):
    message = input().strip()
    if ' ' in message:
        msg, num = message.split()
    else:
        msg = message
    
    if msg == 'push':
        que.append(int(num))
    elif msg == 'pop':
        if que:
            print(que.popleft())
        else:
            print(-1)
    elif msg == 'size':
        print(len(que))
    elif msg == 'empty':
        if que:
            print(0)
        else:
            print(1)
    elif msg == 'front':
        if que:
            print(que[0])
        else:
            print(-1)
    elif msg == 'back':
        if que:
            print(que[-1])
        else:
            print(-1)
