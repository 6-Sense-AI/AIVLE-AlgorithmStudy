import sys
from collections import deque

input = sys.stdin.readline

lst = [deque(input().strip()) for i in range(5)]

ans = ''


for _ in range(15):
    for l in lst:
        if l:
            ans += l.popleft()
        else:
            continue


print(ans)
