import sys
input = sys.stdin.readline

arr_n = int(input()) # 배열의 길이
arr = list(map(int,input().split())) # 배열

chk_n = int(input()) # 비교할 정수의 수
chk = list(map(int,input().split())) # 비교 정수

arr.sort() #오름차순 정렬

for i in range(chk_n):
    st = 0
    end = arr_n-1
    flag = 0
    while st<=end:
        mid = (st+end)//2

        if arr[mid] == chk[i]:
            flag = 1
            print(1)
            break
        elif arr[mid] > chk[i]:
            end = mid-1
        else : st = mid+1
    if flag == 0: print(0)