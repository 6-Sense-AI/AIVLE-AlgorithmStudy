import sys
input = sys.stdin.readline

# 빙글빙글 달팽이

n = int(input()) # 값이자 cnt
find = int(input())

num = n*n #최대값

arr = [ [1]*n for i in range(n)]

tmp = 1 # 상하좌우 구분
base = 0 # base
while 1 :
    if num == 1 : break
    t = tmp % 4 # 4로 나눔

    if t == 1: # 아래
        for i in range(base,n):
            arr[i][base] = num
            num -= 1

    elif t == 2: # 우
        for i in range(1+base,n):
            arr[n-1][i] = num
            num -= 1

    elif t == 3 : #위
        for i in range(n-2,base-1,-1):
            arr[i][n-1] = num
            num -= 1

            if i == base: # 위인 경우 도는 n의 수 -1
                n -= 1

    else : # 좌
        for i in range(n-1,base-1,-1):
            if arr[base][i] == 1:
                arr[base][i] = num
                num -= 1

            if i == base: # 왼쪽이 끝나면 base (x좌표 + 1)
                base += 1
    tmp += 1

f1,f2=0,0 # find 좌표
for i in range(len(arr)):
    for j in range(len(arr)):
        if arr[i][j] == find : f1,f2 = i+1,j+1 # 찾는 수면 저장
        print(arr[i][j], end=' ')
    print()
print(f1,f2)