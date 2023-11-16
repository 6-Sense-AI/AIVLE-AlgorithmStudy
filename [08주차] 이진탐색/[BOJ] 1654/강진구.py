import sys

input = sys.stdin.readline

k, n = map(int, input().split())

lan = [int(input()) for _ in range(k)]

def binary_search(lst, start, end, target):
    mid = (start+end)//2
    cnt = 0
    for l in lst:
        cnt += (l // mid)
    
    if cnt == target:
        return mid
    
    else:
        if cnt < target:
            binary_search(lst, start, mid - 1, target)
        elif cnt > target:
            binary_search(lst, mid + 1, end, target)
        else:
            return -1

binary_search(lan, 0, max(lan), n)
