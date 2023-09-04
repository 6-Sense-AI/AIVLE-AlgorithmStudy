import sys

input = sys.stdin.readline

n = int(input())

target = int(input())

lst = [[0 for _ in range(n)] for _ in range(n)]

r,c = n//2, n//2
lst[r][c] = 1
# 위 오른쪽 아래 왼쪽
k = 2

dr = [-1,0,1,0]
dc = [0,1,0,-1]
i = 0
while k<=int(n**2):
    i %= 4

    if 0<=r+dr[i]<n and 0<=c+dc[i]<n:
        r += dr[i]
        c += dc[i]
    
    if lst[r][c] == 0:
        lst[r][c] = k
    else:
        if i == 0 and 0<=(r+1)<n and 0<=(c-1)<n and lst[r+1][c-1] == 0:
            r += 1
            c -= 1
            lst[r][c] = k
            i = 3
        elif i == 1 and 0<=(r-1)<n and 0<=(c-1)<n and lst[r-1][c-1] == 0:
            c -= 1
            r -= 1
            lst[r][c] = k
            i = 0
        elif i == 2 and 0<=(r-1)<n and 0<=(c+1)<n and lst[r-1][c+1] == 0:
            r -= 1
            c += 1
            lst[r][c] = k
            i = 1
        elif i == 3 and 0<=(r+1)<n and 0<=(c+1)<n and lst[r+1][c+1] == 0:
            c += 1
            r += 1
            lst[r][c] = k
            i = 2
        
    
    k += 1
    i += 1
row,col = 0,0

for i in range(n):
    for j in range(n):
        if lst[i][j] == target:
            row, col = i+1, j+1
        print(lst[i][j], end = ' ')
    print()    
        
print(row, col)