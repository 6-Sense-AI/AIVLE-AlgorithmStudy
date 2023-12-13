import sys
input = sys.stdin.readline
from collections import deque
# 시도2 : 위상정렬 공부 이후

n, m =map(int, input().split())

in_arr = [0] * (n+1) #진입차수 리스트
info = [[] for i in range(n+1)] # 배열 리스트

for i in range(m):
    a, b = map(int,input().split())
    info[a].append(b) # a->b 이동
    in_arr[b] += 1

def topology_sort(): # 위상 정렬
    ans = []
    q=deque()
    for i in range(1, n+1):
        if in_arr[i] == 0: # 시작점
            q.append(i)
    while q: # q가 다 사라질때 까지
        now = q.popleft()
        ans.append(now)
        for i in info[now]:
            in_arr[i] -= 1 # 진입차수 줄여
            if in_arr[i] == 0:
                q.append(i) # q에 넣기
    for i in ans:
        print(i, end=' ')

topology_sort()
