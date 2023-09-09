import sys

input = sys.stdin.readline

n = int(input())

A = list(map(int, input().split()))

m = int(input())

B = list(map(int, input().split()))

A.sort()

ans = []

for target in B:
    st = 0
    end = n-1

    while st<=end:
        mid = (st+end)//2
        if A[mid] == target:
            ans.append(1)
            break
        else:
            if A[mid]<target:
                st = mid+1
            else:
                end = mid-1
    if st>end:
        ans.append(0)

for a in ans:
    print(a)