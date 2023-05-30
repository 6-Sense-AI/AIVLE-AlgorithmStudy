# 이분 탐색 문제

import sys
input = sys.stdin.readline

n = int(input())
cards = list(map(int, input().split()))
m = int(input())
checks = list(map(int, input().split()))

cards.sort()
def binary_search(array, target):
    start, end = 0, n - 1
    
    while start <= end:
        mid = (start + end) // 2
        if array[mid] == target:
            return True
        elif array[mid] > target:
            end = mid - 1
        else:
            start = mid + 1
    return False
            
for c in checks:
    if binary_search(cards, c):
        print(1, end=' ')
    else:
        print(0, end=' ')