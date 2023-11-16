import sys
input = sys.stdin.readline
n, k = map(int,input().split())
data = []
test = []
for _ in range(n):
    a = int(input())
    data.append(a)
length = len(data) 

data.sort()
for i in range(1, max(data)+1):
    x = 0
    for j in range(length):
        x = x + data[j] // i 
    if x == k:
        test.append(i)

x_len = len(test)

print(test[x_len-1])
