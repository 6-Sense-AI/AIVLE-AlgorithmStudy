# n일 동안 m번만 인출해서 사용할 건데 한번 인출 할때 k원씩 k구하기

import sys

input = sys.stdin.readline

n,m = map(int, input().split())

cost = [int(input()) for _ in range(n)]

st, end = min(cost), sum(cost)
ans = 0
while st<=end:
    mid = (st+end)//2
    charge = mid
    cnt = 1
    for c in cost:
        if charge < c:
            cnt += 1
            charge = (st+end)//2
        charge -= c

    
    if cnt > m or mid < max(cost):
        st = mid + 1
    else:
        end = mid - 1
        ans = mid

print(ans)

# for문 다음에 if 문으로 cnt == m일때 mid값을 반환하고 break문 걸면 틀린것으로 나오는데 어떤게 틀렸을까요