# 어렵네요.. dfs로 만들 생각을 안하면 풀기 어려워서 답을 찾아 봤습니다
import sys

input = sys.stdin.readline

def check():
    for i in range(n):
        now = i
        for j in range(h):
            if ladder[j][now] == 1:
                now += 1
            elif now > 0  and ladder[j][now-1] == 1:
                now -= 1
        if now != i:
            return False
    return True

def dfs(r,c,cnt):
    global ans
    if check():
        ans = min(ans, cnt)
        return
    elif cnt == 3 or ans <= cnt:
        return
    
    for i in range(r,h):
        if i == r:
            now = c
        else:
            now = 0
        
        for j in range(now,n-1):
            if ladder[i][j] == 0 and ladder[i][j+1] == 0:
                if j > 0 and ladder[i][j-1] == 1:
                    continue
                ladder[i][j] = 1
                dfs(r,c+2,cnt+1)
                ladder[i][j] = 0

n,m,h = map(int, input().split())
ladder = [[0]*n for _ in range(h)]

for _ in range(m):
    a,b = map(int, input().split())
    ladder[a-1][b-1] = 1

ans = 4
dfs(0,0,0)
print(ans if ans<4 else -1)