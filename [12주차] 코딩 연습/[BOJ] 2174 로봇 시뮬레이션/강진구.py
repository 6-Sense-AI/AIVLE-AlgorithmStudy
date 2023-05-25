from collections import defaultdict, deque
import sys

input = sys.stdin.readline

a,b = map(int, input().split())
n,m = map(int, input().split())

land = [[0 for _ in range(a)] for _ in range(b)]
robot = defaultdict(deque)
command=[]

for i in range(1, n+1):
    st_c,st_r,d = input().split()
    robot[i].append((b-int(st_r),int(st_c)-1,d))
    land[b-int(st_r)][int(st_c)-1] = i
    
for _ in range(m):
    i,c,n = input().split()
    command.append((int(i),c,int(n)))

direction = {'N':(-1,0),'S':(1,0), 'E':(0,1), 'W':(0,-1)}

def change_dir(com,d):
    if com=='L':
        if d=='N':
            d='W'
        elif d=='W':
            d='S'
        elif d=='S':
            d='E'
        else:
            d='N'
    elif com=='R':
        if d=='N':
            d='E'
        elif d=='E':
            d='S'
        elif d=='S':
            d='W'
        else:
            d='N'
    else:
        pass
    return d
error_code = []

for r,c,n in command:
    if error_code:
        break
    elif c == 'F':
        for _ in range(n):
            if robot[r]:
                row, col, d = robot[r].popleft()
                land[row][col] = 0
                dr,dc = direction[d]
                if 0<=row+dr<b and 0<=col+dc<a:
                    row += dr
                    col += dc
                    if land[row][col] != 0:
                        error_code.append(f'Robot {r} crashes into robot {land[row][col]}')
                        break
                    else:
                        robot[r].append((row,col,d))
                        land[row][col] = r
                else:
                    error_code.append(f'Robot {r} crashes into the wall')
                    break
            else:
                break
    else:
        for _ in range(n):
            if robot[r]:    
                row, col, d = robot[r].popleft()
                d = change_dir(c,d)
                robot[r].append((row,col,d))
            else:
                break

if error_code:
    print(error_code[0])
else:
    print('OK')
