import sys
input = sys.stdin.readline

g = int(input())

be, af = 1, 1
max = 100000
result = []

while be<= max and af <= max:
    tmp = af ** 2 - be ** 2

    if tmp == g:
        result.append(be)
    if tmp < g:
        af += 1
        continue
    be += 1

if result: print(*result, sep = '\n')
else: print(-1)