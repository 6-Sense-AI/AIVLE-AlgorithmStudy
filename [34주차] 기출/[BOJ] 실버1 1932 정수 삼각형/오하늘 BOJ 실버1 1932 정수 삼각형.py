import sys
input = sys.stdin.readline
# 누적합인듯
n = int(input())

info = []
for i in range(n):
    info.append(list(map(int,input().split())))

for i in range(1,n):
    for j in range(len(info[i])):
        if j == 0: # 맨 왼쪽이면
            info[i][j] = info[i-1][j]+info[i][j]
        elif j == len(info[i])-1 : # 맨 오른쪽이면
            info[i][j] = info[i-1][len(info[i])-2]+info[i][j]
        else : # 그 사이인 경우
            info[i][j] = max(info[i-1][j-1]+info[i][j], info[i-1][j]+info[i][j])

print(max(info[n-1]))