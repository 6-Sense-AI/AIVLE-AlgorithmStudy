'''
비어있는 칸 중에서 좋아하는 학생이 인접한 칸에 가장 많은 칸으로 자리를 정한다.
1을 만족하는 칸이 여러 개이면, 인접한 칸 중에서 비어있는 칸이 가장 많은 칸으로 자리를 정한다.
2를 만족하는 칸도 여러 개인 경우에는 행의 번호가 가장 작은 칸으로, 그러한 칸도 여러 개이면 열의 번호가 가장 작은 칸으로 자리를 정한다.
'''
import sys
from collections import deque, Counter

input = sys.stdin.readline

n = int(input())

que = deque([])

for _ in range(int(n**2)):
    s1, s2, s3, s4, s5 = map(int, input().split())
    que.append((s1,s2,s3,s4,s5))

arr = [[0 for _ in range(n)] for _ in range(n)]

def nearby(idx):
    r,c = idx
    near=[]
    dr = [0,0,1,-1]
    dc = [1,-1,0,0]
    for i in range(4):
        nr = r+dr[i]
        nc = c+dc[i]
        if 0<=nr<n and 0<=nc<n:
            near.append(nr,nc)
    
    return near

def find_blank(idx):
    r,c = idx
    blank = []
    dr = [0,0,1,-1]
    dc = [1,-1,0,0]
    for i in range(4):
        nr = r+dr[i]
        nc = c+dc[i]
        if 0<=nr<n and 0<=nc<n and arr[nr][nc]==0:
            blank.append((nr,nc))
    # 빈칸이 주변에 가장 많은거 찾기
    rank = Counter(blank)
    mode = rank.most_common()
    maximum = mode[0][1]
    # 겹치면 여러개 넣기
    modes = []
    for m in mode:
        if m[1] == maximum:
            modes.append(m[0])
    return modes

s1,s2,s3,s4,s5 = que.popleft()

arr[n//2][n//2] = s1

while que:
    s1,s2,s3,s4,s5 = que.popleft()
    
    near_lst = []

    if s2 in arr:
        for i in range(n):
            c = arr[i].find(s2)
            near = nearby(i,c)
            near_lst.extend(near)
            
    if s3 in arr:
        for i in range(n):
            c = arr[i].find(s3)
            near = nearby(i,c)
            near_lst.extend(near)
            
    if s4 in arr:
        for i in range(n):
            c = arr[i].find(s4)
            near = nearby(i,c)
            near_lst.extend(near)
            
    if s5 in arr:
        for i in range(n):
            c = arr[i].find(s5)
            near = nearby(i,c)
            near_lst.extend(near)
    
    c = Counter(near_lst)
    cmc = c.most_common()
    ms = []
    if cmc:
        for i,cm in enumerate(cmc):
            if arr[cm[0][0]][cm[0][1]] == 0:
                maximum = order[0][1]

                modes = []
                for num in order:
                    if num[1] == maximum:
                        modes.append(num[0])

                ms = find_blank(modes)
                if len(ms)>1:
                    ms.sort(key = lambda x:(x[0],x[1]))
                arr[ms[0][0]][ms[0][1]] = s1
                break
    else:
        mm = 0
        row,col = 0,0
        for i in range(n):
            for j in range(n):
                if max(mm,find_blank((i,j))[0][1]) == find_blank((i,j))[0][1]:
                    mm = find_blank((i,j))[0][1]
                    row,col = i,j
        arr[row][col] = s1
print(arr)