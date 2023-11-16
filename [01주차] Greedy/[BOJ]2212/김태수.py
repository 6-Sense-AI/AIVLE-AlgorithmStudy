import sys
input = sys.stdin.readline

n = int(input())
k = int(input())
sen = list(map(int, input().split()))
sen.sort()

gap = []
for i in range(0, n-1):
    gap.append(sen[i+1]-sen[i])
    
gap.sort()
print(sum(gap[:n-k]))
