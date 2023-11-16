import sys

input = sys.stdin.readline

k, n = map(int, input().split())

lan = [int(input()) for _ in range(k)]

def binary_search(lst, start, end, target):
    if start > end:
        return end  # 랜선 길이의 최댓값 반환
    
    mid = (start+end)//2
    cnt = 0
    for l in lst:
        cnt += (l // mid)
    
    if cnt < target:
        return binary_search(lst, start, mid - 1, target)
    else:  # cnt >= target
        return binary_search(lst, mid + 1, end, target)

print(binary_search(lan, 1, max(lan), n))
