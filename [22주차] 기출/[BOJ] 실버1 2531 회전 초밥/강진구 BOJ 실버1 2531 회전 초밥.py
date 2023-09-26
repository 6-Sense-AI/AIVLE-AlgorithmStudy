# 가지 수가 가장 많게
import sys

input = sys.stdin.readline

n, d, k, c = map(int, input().split())

sushi = [int(input()) for _ in range(n)]

sushi += sushi[:k]

max_t = 0

for i in range(n):
    t = set(sushi[i:i+k])
    
    if c in t:
        max_t = max(max_t, len(t))
    else:
        max_t = max(max_t, len(t)+1)


print(max_t)