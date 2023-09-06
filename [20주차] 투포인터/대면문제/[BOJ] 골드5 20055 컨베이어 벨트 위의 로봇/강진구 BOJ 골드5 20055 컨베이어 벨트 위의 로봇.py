import sys
from collections import deque

input = sys.stdin.readline

n, k = map(int, input().split())

lst = list(map(int, input().split()))

conv = [[0 for _ in range(n)],[0 for _ in range(n)]]
d = [[],[]]
for i,l in enumerate(lst):
    if i < n:
        d[0].append(l)
    else:
        d[1].append(l)


'''
벨트가 각 칸 위에 있는 로봇과 함께 한 칸 회전한다.
가장 먼저 벨트에 올라간 로봇부터, 벨트가 회전하는 방향으로 한 칸 이동할 수 있다면 이동한다. 만약 이동할 수 없다면 가만히 있는다.
로봇이 이동하기 위해서는 이동하려는 칸에 로봇이 없으며, 그 칸의 내구도가 1 이상 남아 있어야 한다.
올리는 위치에 있는 칸의 내구도가 0이 아니면 올리는 위치에 로봇을 올린다.
내구도가 0인 칸의 개수가 K개 이상이라면 과정을 종료한다. 그렇지 않다면 1번으로 돌아간다.
'''

def f_1(arr):
    for i in range(2):
        if i == 0:
            que = deque(arr[i])
            que.appendleft(0)
            que.pop()
        else:
            que = deque(arr[i])
            que.append(0)
            que.popleft()
        arr[i] = list(que)
    return arr
            
def f_2(arr, d):
    flag = 0
    for i in range(2):
        if i == 0:
            for j in range(n):
                if d[j] == 0 and 0<=j-1 and arr[j-1]==1:
                    if 0<=j-2 and arr[j-2] == 0:
                        arr[j-2] = 1
                        arr[j-1] = 0
                    else:
                        flag += 1
                        break
        else:
            for j in range(n-1,-1,-1):
                if d[j] == 0 and j+1<n and arr[j+1]==1:
                    if j+2<n and arr[j+2] == 0:
                        arr[j+2] = 1
                        arr[j+1] = 0
                    else:
                        flag += 1
                        break
    if flag == 0:
        arr_ = f_1(arr)
    else:
        arr_ = arr
    return arr_

def f_3(arr, d):
    if d[0][0] != 0:
        arr[0][0] = 1
    
    if d[1][n-1] != 0:
        arr[1][n-1] = 1
    
    return arr

def f_4(d, k):
    cnt = 0
    for i in range(2):
        cnt += d[i].count(0)
    
    if cnt >= k:
        return False
    else:
        return True

f_cnt = 0
while f_4:
    if f_1(conv) != conv:
        f_cnt+=1
        f_1(conv)
    if f_2(conv, d) != conv:
        f_cnt+=1
        f_2(conv,d)
    if f_3(conv, d) != conv:
        f_cnt+=1
        f_3(conv,d)
    if f_4(d, k):
        f_cnt+=1
        f_4(d, k)
print(f_cnt)
