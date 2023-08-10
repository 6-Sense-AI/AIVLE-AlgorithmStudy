import sys
input = sys.stdin.readline

# 입력받기
com = int(input())
num = int(input())

# 그래프 선언 및 연결
graph = [[] for i in range(com + 1)]
for _ in range(num):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

# 컴퓨터 수
cnt = 0

# 컴퓨터 수를 찾기위한 dfs 함수 생성
def dfs(v):
    global cnt
    visited[v] = True
    for i in graph[v]:
        if not visited[i]:
            dfs(i)
            cnt += 1

visited = [False] * (com+1)
dfs(1)
print(cnt)
