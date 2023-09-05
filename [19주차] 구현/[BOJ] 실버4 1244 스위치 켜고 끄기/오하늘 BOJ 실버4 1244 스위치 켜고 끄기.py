import sys
input = sys.stdin.readline

n = int(input()) # 스위치 수
arr = list(map(int,input().split())) # 배열
cnt = int(input()) # 학생 수

for i in range(cnt):
    s, c = map(int, input().split())

    if s == 1: # 남학생
        c1 = c
        # 배수
        while 1:
            if c>n: break

            if arr[c-1] == 1 : arr[c-1] = 0 
            else : arr[c-1] = 1

            c += c1 # 배수 곱하기

    else : # 여학생
        if arr[c-1] == 1 : arr[c-1] = 0 
        else : arr[c-1] = 1

        c1, c2 = c-1, c+1 # 양 옆

        while 1 :
            if c1 <= 0 or c2 > n : break # 범위 벗어남
            if arr[c1-1] != arr[c2-1] : break # 다름

            if arr[c1-1] == 1 :
                arr[c1-1] = 0
                arr[c2-1] = 0

            else :
                arr[c1-1] = 1
                arr[c2-1] = 1
            
            c1 -= 1
            c2 += 1

cnt = 1
for i in range(n): 
    print(arr[i], end=' ')
    if cnt%20 == 0 : print()
    cnt += 1
