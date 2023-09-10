import sys
input = sys.stdin.readline

# n: 수열의 길이, target: 만들고자 하는 합
n, target = map(int, input().split())
nlist = list(map(int, input().split()))    # 수열
ans = 0    # 경우의 수

left, right = 0, 1
while left <= right and right <= n:
    now = sum(nlist[left:right])    # 현재 합
    
    if now == target:
        ans += 1
        right += 1
    elif now < target:
        right += 1
    else:
        left += 1

print(ans)