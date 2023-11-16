import sys

input = sys.stdin.readline

k, n = map(int, input().split())
len = []

for _ in range(k):
    l = int(input())
    len.append(l)

len.sort()
cnt = 0

while cnt != n:
    a = len[0]
    
    for i in len:
        cnt += i // a
    
    if cnt == n:
        print(a)
        break
    
    elif cnt > n :
        a += (len[0]//2)
     
    else:
        a -= (len[0]//2)
