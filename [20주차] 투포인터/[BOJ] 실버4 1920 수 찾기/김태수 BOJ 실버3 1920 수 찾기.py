import sys
input = sys.stdin.readline

n = int(input())
data1 = list(map(int,input().split()))
m = int(input())
data2 = list(map(int,input().split()))

data1.sort()

def binary(num):
    left = 0
    right = n -1

    while left <= right:
        mid = (left + right) // 2
        if data1[mid] == num:
            return True
        
        if num < data1[mid]:
            right = mid - 1
        elif num > data1[mid]:
            left = mid + 1

for i in range(m):
    if binary(data2[i]):
        print(1)
    else:
        print(0)