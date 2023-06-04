n, k = map(int, input().split())

lst = [i for i in range(1,n+1)]

i = k-1
ans = []
while lst:
    ans.append(lst.pop(i))
    if i+k-1 < len(lst):
        i += k-1
    else:
        if len(lst) < i+k-1 < (2*len(lst)):
            i = i+k-1-len(lst)
        elif i+k>=(2*len(lst)):
            i = i+k-1-2*len(lst)

for i,a in enumerate(ans):
    if i==0:
        print('<',end='')
        print(a,end=', ')
    elif 0<i<len(ans)-1:
        print(a, end=', ')
    else:
        print(a, end='>')
    
