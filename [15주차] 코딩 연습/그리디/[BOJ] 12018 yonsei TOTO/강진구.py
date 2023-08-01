from collections import defaultdict

n, m = map(int, input().split())

d = defaultdict(list)

c_lst = []

for i in range(2*n):
    if i%2 == 0:
        d[i].append(list(map(int, input().split())))
    else:
        d[i-1].append(sorted(map(int, input().split()), reverse=True))
        p1 = d[i-1][0][0]
        p2 = d[i-1][0][1]
        if p1<p2:
            c_lst.append((i-1,1))
        else:
            c_lst.append((i-1,d[i-1][1][p2-1]))

ans = 0
c_lst.sort(key=lambda x:x[1])


for _,c in c_lst:
    if m >= c:
        m -= c
        ans += 1
    else:
        break

print(ans)
