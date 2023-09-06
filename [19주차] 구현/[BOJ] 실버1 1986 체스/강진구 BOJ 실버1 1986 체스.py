import sys

input = sys.stdin.readline

n, m = map(int, input().split())

q_lst = list(map(int, input().split()))

k_lst = list(map(int, input().split()))

p_lst = list(map(int, input().split()))

board = [[0 for _ in range(m)] for _ in range(n)]

row, col = [],[]
for i,p in enumerate(p_lst):
    if i == 0:
        continue
    else:
        if i%2 != 0:
            row.append(p-1)
        else:
            col.append(p-1)

for r,c in zip(row,col):
    board[r][c] = 1 #pawn은 1로

k_row, k_col = [],[]
for i,p in enumerate(k_lst):
    if i == 0:
        continue
    else:
        if i%2 != 0:
            k_row.append(p-1)
        else:
            k_col.append(p-1)

for r,c in zip(k_row,k_col):
    board[r][c] = 2 # knight는 2로
    

row, col = [],[]
for i,p in enumerate(q_lst):
    if i == 0:
        continue
    else:
        if i%2 != 0:
            row.append(p-1)
        else:
            col.append(p-1)

for r,c in zip(row, col):
    board[r][c] = 3 # queen은 3으로

# queen 있는 행 열 대각선 다 못감 근데 방해물 있으면 체크
for r in row:
    if 1 in board[r]:
        idx_1 = board[r].index(1)
        idx_3 = board[r].index(3)
        if idx_1>idx_3:
            for i in range(idx_3+1,m):
                if board[r][i] == 3 or board[r][i] == 1:
                    continue
                board[r][i] = -1
        else:
            for i in range(idx_1+1,m):
                if board[r][i] == 3 or board[r][i] == 1:
                    continue
                board[r][i] = -1
    
    elif 2 in board[r]:
        idx_2 = board[r].index(2)
        idx_3 = board[r].index(3)
        if idx_2>idx_3:
            for i in range(idx_3+1,m):
                if board[r][i] == 3 or board[r][i] == 2:
                    continue
                board[r][i] = -1
        else:
            for i in range(idx_2+1,m):
                if board[r][i] == 3 or board[r][i] == 2:
                    continue
                board[r][i] = -1
    
    else:
        for b in board[r]:
            if b == 3:
                continue
            else:
                b = -1

for r,c in zip(row, col):
    for i in range(n):
        if board[i][c] == 1 or board[i][c] == 2:
            if i > r:
                for j in range(r+1,i):
                    board[j][c] = -1
            else:
                for j in range(i+1,r):
                    board[j][c] = -1
        else:
            if board[i][c] != 3:
                board[i][c] = -1

for r,c in zip(row, col):
    for i,j in zip(range(r-1,-1,-1),range(c+1,m)):
        if board[i][j] == 0:
            board[i][j] = -1
        else:
            if board[i][j] == 3:
                continue
            else:
                break
    for i,j in zip(range(r-1,-1,-1),range(c-1,-1,-1)):
        if board[i][j] == 0:
            board[i][j] = -1
        else:
            if board[i][j] == 3:
                continue
            else:
                break
    for i,j in zip(range(r+1,n),range(c+1,m)):
        if board[i][j] == 0:
            board[i][j] = -1
        else:
            if board[i][j] == 3:
                continue
            else:
                break
    for i,j in zip(range(r+1,n),range(c-1,-1,-1)):
        if board[i][j] == 0:
            board[i][j] = -1
        else:
            if board[i][j] == 3:
                continue
            else:
                break

# knight는 대각선 23으로만 가능(r+-1,c+-2)(r+-2,c+-1)
for r,c in zip(k_row,k_col):
    if 0<=r-2<n and 0<=c-1<m and board[r-2][c-1] == 0:
        board[r-2][c-1] = -1
    if 0<=r-1<n and 0<=c-2<m and board[r-1][c-2] == 0:
        board[r-1][c-2] = -1
    if 0<=r+1<n and 0<=c-2<m and board[r+1][c-2] == 0:
        board[r+1][c-2] = -1
    if 0<=r+2<n and 0<=c-1<m and board[r+2][c-1] == 0:
        board[r+2][c-1] = -1
    if 0<=r+2<n and 0<=c+1<m and board[r+2][c+1] == 0:
        board[r+2][c+1] = -1
    if 0<=r+1<n and 0<=c+2<m and board[r+1][c+2] == 0:
        board[r+1][c+2] = -1
    if 0<=r-1<n and 0<=c+2<m and board[r-1][c+2] == 0:
        board[r-1][c+2] = -1
    if 0<=r-2<n and 0<=c+1<m and board[r-2][c+1] == 0:
        board[r-2][c+1] = -1

ans = 0
for i in range(n):
    ans += board[i].count(0)

print(ans)