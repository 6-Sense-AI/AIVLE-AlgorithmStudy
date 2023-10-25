# 예제는 다 맞는데 틀렸다,,,
import sys
input = sys.stdin.readline
from collections import deque

n, m = map(int,input().split())
graph = []
result = [] ##결과 저장을 위한 리스트생성
for _ in range(n):
    graph.append(list(map(int,input().split())))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def one(x,y,graph):
    if y < m and y+3 < m:
        num = graph[x][y] + graph[x][y+1] + graph[x][y+2] + graph[x][y+3]
        result.append(num)
    if x < n and x+3 < n:
        num = graph[x][y] + graph[x+1][y] + graph[x+2][y] + graph[x+3][y]
        result.append(num)

def two(x,y,graph):
    if x>=0 and x+2<n and y>=0 and y+1<m:
        num = graph[x][y]+graph[x+1][y]+graph[x+2][y]+graph[x+2][y+1]
        result.append(num)
    if x>=0 and x+1<n and y>=0 and y+2<m:
        num = graph[x][y]+graph[x][y+1]+graph[x][y+2]+graph[x+1][y]
        result.append(num)
    if x>=0 and x+2<n and y>=0 and y+1<m:
        num = graph[x][y]+graph[x][y+1]+graph[x+1][y+1]+graph[x+2][y+1]
        result.append(num)
    if x-1>=0 and x<n and y>=0 and y+2<m:
        num = graph[x][y]+graph[x][y+1]+graph[x][y+2]+graph[x-1][y+2]
        result.append(num)
    if x-2>=0 and x<n and y>=0 and y+1<m:
        num = graph[x][y]+graph[x][y+1]+graph[x-1][y+1]+graph[x-2][y+1]
        result.append(num)
    if x>=0 and x+1<n and y>=0 and y+2<m:
        num = graph[x][y]+graph[x][y+1]+graph[x][y+2]+graph[x+1][y+2]
        result.append(num)
    if x>=0 and x+2<n and y>=0 and y+1<m:
        num = graph[x][y]+graph[x][y+1]+graph[x+1][y]+graph[x+2][y]
        result.append(num)
    if x>=0 and x+1<n and y>=0 and y+2<m:
        num = graph[x][y]+graph[x+1][y]+graph[x+1][y+1]+graph[x+1][y+2]
        result.append(num)

def three(x,y,graph):
    if x>=0 and x+2<n and y>=0 and y+1<m:
        num = graph[x][y]+graph[x+1][y]+graph[x+1][y+1]+graph[x+2][y+1]
        result.append(num)
    if x-1>=0 and x<n and y>=0 and y+2<m:
        num = graph[x][y]+graph[x][y+1]+graph[x-1][y+1]+graph[x-1][y+2]
        result.append(num)
    if x-1>=0 and x+1<n and y>=0 and y+1<m:
        num = graph[x][y]+graph[x+1][y]+graph[x][y+1]+graph[x-1][y+1]
        result.append(num)
    if x>=0 and x+1>n and y>=0 and y+2<m:
        num = graph[x][y]+graph[x][y+1]+graph[x+1][y+1]+graph[x+1][y+2]
        result.append(num)

def four(x,y,graph):
    if x>=0 and x+1<n and y>=0 and y+2<m:
        num = graph[x][y]+graph[x][y+1]+graph[x][y+2]+graph[x+1][y+1]
        result.append(num)
    if x-1>=0 and x<n and y>=0 and y+2<m:
        num = graph[x][y]+graph[x][y+1]+graph[x-1][y+1]+graph[x][y+2]
        result.append(num)
    if x-1>=0 and x+1<n and y>=0 and y+1<m:
        num = graph[x][y]+graph[x][y+1]+graph[x-1][y+1]+graph[x+1][y+1]
        result.append(num)
    if x>=0 and x+2<n and y>=0 and y+1<m:
        num = graph[x][y]+graph[x+1][y]+graph[x+2][y]+graph[x+1][y+1]
        result.append(num)

def five(x,y,graph):
    if x>=0 and x+1<n and y>=0 and y+1<m:
        num = graph[x][y]+graph[x][y+1]+graph[x+1][y]+graph[x+1][y+1]
        result.append(num)

for i in range(n):
    for j in range(m):
        one(i,j,graph)
        two(i,j,graph)
        three(i,j,graph)
        four(i,j,graph)
        five(i,j,graph)

print(max(result))