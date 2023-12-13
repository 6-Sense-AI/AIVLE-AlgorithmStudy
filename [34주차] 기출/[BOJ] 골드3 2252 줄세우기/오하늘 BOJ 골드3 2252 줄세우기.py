import sys
input = sys.stdin.readline
# 시도1 : 스위치 방법. 나열해놓고, 그 순서가 등장하면 자리를 바꾼다.
# 결과 시간초과
n, m =map(int, input().split())

arr = []
for i in range(n):
    arr.append(i+1)

for i in range(m):
    a, b = map(int, input().split())
    t1 = arr.index(a) # 전
    t2 = arr.index(b) # 후

    if t1 > t2 :
        tmp = arr[t1]
        arr[t1] = arr[t2]
        arr[t2] = tmp

for i in range(len(arr)):
    if i == len(arr)-1:
        print(arr[i])
    else: print(arr[i], end=' ')