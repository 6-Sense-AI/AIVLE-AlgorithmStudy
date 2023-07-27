import sys
input = sys.stdin.readline
from collections import deque

lst = list(input().strip())
dq = deque(lst) # 데큐 사용
ans = ''

while dq:
    if dq[0] == '<' : # 우선 조건 1 : 태그는 그대로
        while 1 :
            if dq[0] == '>':
                ans += str(dq.popleft())
                break
            else : ans += str(dq.popleft())

    if len(dq) == 0:
        break

    if dq[0] == ' ' : # 조건 2 : 공백의 경우 뒤집어준다
        ans += str(dq.popleft()) # start 공백
        tmp = "" # 임시 데큐 생성
        while 1 :
            if len(dq) == 0:
                ans += tmp[::-1]
                break
            if dq[0] == ' ': # end 공백
                ans += tmp[::-1]
                ans += str(dq.popleft()) # 마지막 공백
                break
            else :
                tmp += str(dq.popleft())
    
    if len(dq) == 0:
        break
    
    else : # 조건3 : 평문
        tmp = "" # 임시 데큐 생성
        while 1 :
            if len(dq) == 0:
                ans += tmp[::-1]
                break 
            if dq[0] == ' ' or dq[0] =='<':
                ans += tmp[::-1]
                break
            else :
                tmp += str(dq.popleft())
    if len(dq) == 0:
        break

print(ans)
