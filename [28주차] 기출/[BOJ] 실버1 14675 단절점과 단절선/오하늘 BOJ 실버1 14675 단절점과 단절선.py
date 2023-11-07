import sys
input = sys.stdin.readline

# 처음에는 그냥 리스트에 다 넣어서 개수가 1개면 단절점 해줬는데
# 시간초과 떠서 이중 배열로 수정했다.

n = int(input()) #트리의 정점 개수
g = [[] for i in range(n+1)]

for i in range(n-1):
    a, b = map(int,input().split())
    g[a].append(b)
    g[b].append(a)

q = int(input()) #질의의 개수
for i in range(q):
    chk = 0
    t, k = map(int,input().split()) # t=1:점 2:선 , k는 정점
    if t == 1 : # 단절점일때
        if len(g[k]) < 2: # 리프노드면
            print('no')
        else : print('yes')
    else : print('yes')