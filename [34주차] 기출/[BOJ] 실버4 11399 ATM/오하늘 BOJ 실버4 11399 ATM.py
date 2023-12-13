import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int,input().split()))

arr.sort()
ans = 0
total = 0

for i in arr:
    ans += i
    total += ans
print(total)