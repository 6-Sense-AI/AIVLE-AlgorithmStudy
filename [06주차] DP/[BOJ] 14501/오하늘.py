# 퇴사
import sys
input = sys.stdin.readline

n = int(input())

arr = [list(map(int, input().split())) for _ in range(n)]
max = 0

for i in range(len(arr)) :
    j = 0
    sum = 0
    while (1):
        if j+1 + arr[j][0] > n:
            break
        sum += arr[j][1]
        j+=arr[j][0]
    if sum > max:
        max = sum

print(max)
