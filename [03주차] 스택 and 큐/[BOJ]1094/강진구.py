import sys

x = int(sys.stdin.readline())

lst = []
for i in range(7):
    lst.append(2**i)

lst.reverse()
ans = []
for l in lst:
    if l > x:
        continue
    else:
        if sum(ans) == x:
            break
        else:
            if sum(ans) + l <= x:
                ans.append(l)

print(len(ans))
