import sys
input = sys.stdin.readline

n, m, r = map(int,input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
num = list(map(int, input().split()))

def one():
    tmp = [[0] * m for _ in range(n)]
    

def two():
    tmp = [[0] * m for _ in range(n)]
    for i in range(n):
        for j in range(m):
            tmp[i][j] = graph[i][m-j-1]
    return tmp

def three():
    tmp = [[0] * m for _ in range(n)]
    for i in range(n):
        for j in range(m):
            tmp[i][j] = graph[n-j-1][i]
    return tmp

def four():
    tmp = [[0] * m for _ in range(n)]
    for i in range(n):
        for j in range(m):
            tmp[i][j] = graph[j][m-i-1]
    return tmp

def five():
    tmp = [[0] * m for _ in range(n)]
    return tmp

def six():
    tmp = [[0] * m for _ in range(n)]
    return tmp