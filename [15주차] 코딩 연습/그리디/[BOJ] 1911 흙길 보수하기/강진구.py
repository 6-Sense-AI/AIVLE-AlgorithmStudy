n, l = map(int, input().split())

w_idx = []

for _ in range(n):
    w_idx.append(tuple(map(int,input().split())))

ans = 0

w_idx.sort(key = lambda x:(x[0],x[1]))
k = 0

for idx in w_idx:
    st, end = idx
    if st < k:
        st = k
    if ((end-st)/l) == (end-st)//l:
        n = (end-st)/l
    else:
        n = (end-st)//l + 1
    ans += int(n)
    k = st + n*l

print(ans)
