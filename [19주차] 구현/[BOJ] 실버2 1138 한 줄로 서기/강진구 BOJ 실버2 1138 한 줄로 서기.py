import sys
from collections import deque

input = sys.stdin.readline

n = int(input())

memory = list(map(int, input().split()))

# 자기 왼쪽에 자기보다 큰 사람 수 기억

ans = [0]*n

que = deque(memory)

i = 0
while que:
    m = que.popleft()

    if m == 0:
        if ans[i] == 0:
            ans[i] = i+1
        else:
            for j in range(i):
                if ans[j] == 0:
                    ans[j] = i+1
                    break
    else:
        for j in range(m,n):
            if ans[j] == 0 and (ans[:j].count(0) == m):
                ans[j] = i+1
                break
    i += 1

for a in ans:
    print(a, end=' ')

# 왜 안되지?
