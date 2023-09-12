# 어렵다
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
arr = []
for _ in range(n):
    arr.append(int(input()))

left = min(arr)
right = max(arr)

while left <= right:
    mid = (left + right)//2
    now = mid
    cnt = 1

    for i in range(n):
        if now < arr[i]:
            now = mid
            cnt += 1
        now -= arr[i]

    if cnt > m or mid < max(arr):
        left = mid + 1
    else:
        right = mid - 1
        num = mid

print(num)