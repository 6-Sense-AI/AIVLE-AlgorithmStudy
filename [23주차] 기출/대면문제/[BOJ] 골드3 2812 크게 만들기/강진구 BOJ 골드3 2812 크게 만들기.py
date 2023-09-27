import sys
from collections import deque

input = sys.stdin.readline

n, k = map(int, input().split())

num = list(input().strip())

cnt = 0

# k개 중에서 제일 큰거만 남기기

ans = []
que = deque(num)

while que:
    if cnt < k:
        x = que.popleft()

        if x > que[0]:
            ans.append(x)
            cnt += 1
        elif x < que[0]:
            if ans:
                while ans:
                    y = ans.pop()
                    if y>=que[0]:
                        break
                    else:
                        cnt += 1
        else:
            ans.append(x)
            ans.append(x)
            que.popleft()
    else:
        ans += list(que)
        break

print(ans)

