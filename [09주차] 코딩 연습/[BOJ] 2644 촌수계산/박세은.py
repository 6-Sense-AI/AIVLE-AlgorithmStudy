n = int(input())
a, b = map(int, input().split())
m = int(input())
lst = [[] for _ in range(n)]

for _ in range(m):
    x, y = map(int, input().split())
    lst[x-1].append(y)
    
cnt = 0

for i in lst:
    for j in range(len(i)):
        num = i[j]
        if i[j] == :
