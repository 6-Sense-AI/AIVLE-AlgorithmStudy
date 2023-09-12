import sys

input = sys.stdin.readline

g = int(input())

cur, last = 1, 1  # 여기 자연수부터 시작해야함

cur_lst = []

while cur+last <= g:
    sq = (cur+last)*(cur-last)
    
    if sq == g and int(cur) == cur:
        cur_lst.append(cur)
        cur += 1
    elif sq < g:
        cur += 1
    else:
        last += 1

if cur_lst:
    for c in cur_lst:
        print(c)
else:
    print(-1)