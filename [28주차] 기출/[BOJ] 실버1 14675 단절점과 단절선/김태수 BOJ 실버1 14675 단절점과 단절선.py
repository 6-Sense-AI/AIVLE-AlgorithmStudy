# t가 1일때에는 해당 정점에 연결된 정점의 개수를 이용한다.
# t가 2인 경우는 무조건 yes가 나온다
import sys
input = sys.stdin.readline

# 입력받기
n = int(input())
graph = [[] for _ in range(n+1)]

# 그래프 양방향 연결
for _ in range(n-1):
    a, b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)

q = int(input())
for _ in range(q):
    t, k = map(int,input().split())
    if t == 1: # t가 1인경우
        if len(graph[k])==1: 
            print('no')
        else:
            print('yes')
    elif t == 2: # t가 2인경우
        print('yes')