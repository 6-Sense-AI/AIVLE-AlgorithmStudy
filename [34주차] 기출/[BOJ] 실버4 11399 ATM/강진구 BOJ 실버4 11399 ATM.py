import sys
input = sys.stdin.readline

n = int(input())

p = list(map(int,input().split()))

p.sort()
ans = 0

for i in range(1,n+1):
    s = sum(p[:i])
    ans += s

print(ans)