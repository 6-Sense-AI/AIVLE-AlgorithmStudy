import sys
input = sys.stdin.readline

graph = []
n = int(input())
for _ in range(n):
    graph.append(input().split())

for i in range(n):
    for j in range(n):
        if graph[i][j] == 'S' and (graph[i][j-1] or graph[i][j+1] or graph[i-1][j] or graph[i+1][j] == 'T'):
            print('NO')
            break

cnt = 0

for i in range(n):
    if 'S' in graph[i] and 'T' in graph[i]:
        cnt += 1

for j in range(n):
    column = [graph[i][j] for i in range(n)]
    if 'S' in column and 'T' in column:
        cnt += 1

if cnt >= 4:
    print('NO')
else:
    print('YES')