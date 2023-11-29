# 잘못생각함
from collections import deque

n = int(input())
grp = [list(map(int, input().split())) for _ in range(n)]

mxAns = 0
mnAns = float("inf")

que = deque(grp[0])
cnt = -1

while que:
    idx = 1
    x = que.popleft()
    cnt += 1
    mx = x
    mn = x
    now_mx = cnt
    now_mn = cnt

    for _ in range(n-1):
        if now_mx-1 < 0:
            mx += max(grp[idx][now_mx], grp[idx][now_mx+1])
            now_mx = grp[idx].index(max(grp[idx][now_mx], grp[idx][now_mx+1]))

        elif now_mx-1 >= 0 and now_mx+1 < n:
            mx += max(grp[idx][now_mx-1], grp[idx][now_mx], grp[idx][now_mx+1])
            now_mx = grp[idx].index(max(grp[idx][now_mx-1], grp[idx][now_mx], grp[idx][now_mx+1]))

        elif now_mx+1 >= n:
            mx += max(grp[idx][now_mx-1], grp[idx][now_mx])
            now_mx = grp[idx].index(max(grp[idx][now_mx-1], grp[idx][now_mx]))
        
        if now_mn-1 < 0:
            mn += min(grp[idx][now_mn], grp[idx][now_mn+1])
            now_mn = grp[idx].index(min(grp[idx][now_mn], grp[idx][now_mn+1]))

        elif now_mn-1 >= 0 and now_mn+1 < n:
            mn += min(grp[idx][now_mn-1], grp[idx][now_mn], grp[idx][now_mn+1])
            now_mn = grp[idx].index(min(grp[idx][now_mn-1], grp[idx][now_mn], grp[idx][now_mn+1]))

        elif now_mn+1 >= n:
            mn += min(grp[idx][now_mn-1], grp[idx][now_mn])
            now_mn = grp[idx].index(min(grp[idx][now_mn-1], grp[idx][now_mn]))
        
        idx += 1
    
    mxAns = max(mxAns, mx)
    mnAns = min(mnAns, mn)

print(mxAns, mnAns)