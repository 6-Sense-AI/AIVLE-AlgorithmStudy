import sys
n = int(sys.stdin.readline())
k = int(sys.stdin.readline())
n_lst = list(map(int, sys.stdin.readline().split()))

n_lst.sort()
dist = []

for i in range(n-1):
    dist.append(n_lst[i+1]-n_lst[i])

dist.sort()


print(sum(dist[:n-k]))
