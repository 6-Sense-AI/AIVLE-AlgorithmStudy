import sys

input = sys.stdin.readline

n = int(input())
stack = []
for _ in range(n):
    stack.append(int(input()))

num = 0
cnt = 0
for s in stack[::-1]:
    if s > num:
        cnt += 1
        num = s
print(cnt)
