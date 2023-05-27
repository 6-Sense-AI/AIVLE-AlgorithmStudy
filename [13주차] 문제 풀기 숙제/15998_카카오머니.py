import sys
import math

input = sys.stdin.readline

n = int(input())

log = []

for _ in range(n):
    log.append(tuple(map(int, input().split())))

charge = []
m = 0

for l in log:
    a, b = l[0], l[1]
    if a < 0:
        if a+m-b < 0:
            charge.append(abs(a)+b-m)
            m = b
        else:
            m += a
    else:
        m += a
if charge:
    min_v = charge[0]
else:
    min_v = int(10e18)

flag = 0
for c in charge:
    if math.gcd(c, min_v) > 1:
        min_v = min(min_v, math.gcd(c,min_v))
    else:
        flag = 1

if flag == 0:
    print(min_v)
    if not charge:
        print(1)
else:
    print(-1)
