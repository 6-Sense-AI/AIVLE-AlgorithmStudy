import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
cnt = 0

deq = deque() # 데큐 선언
for i in range(0,n):
    deq.append(int(input())) # 완성
v = deq.pop() # 제일 오른쪽이 기준
for _ in range(len(deq)):
    a = deq.pop()
    if a>v:
        v = a # 기준값 갱신
        cnt += 1
print(cnt+1) #본인 포함
