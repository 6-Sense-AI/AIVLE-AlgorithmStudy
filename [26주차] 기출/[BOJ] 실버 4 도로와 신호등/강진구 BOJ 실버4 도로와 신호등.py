import sys
from collections import deque

input = sys.stdin.readline

N, L = map(int, input().split())

que = deque([])

for _ in range(N):
    D,R,G = map(int, input().split())
    que.append((D,R,G))

time = 0
cur = 0
while L>0:
    if que:
        d,r,g = que.popleft()
        if cur == d:
            if time/(r+g)<1:
                if time < r:
                    time += r-time
            else:
                if time%(r+g) < r:
                    time += r-time%(r+g)
        else:
            que.appendleft((d,r,g))
    
    cur += 1
    time += 1
    L -= 1
    
print(time)