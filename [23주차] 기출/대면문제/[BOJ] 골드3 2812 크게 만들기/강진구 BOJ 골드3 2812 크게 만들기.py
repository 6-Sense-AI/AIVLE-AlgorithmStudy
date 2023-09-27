import sys
from collections import deque

input = sys.stdin.readline

n, k = map(int, input().split())

num = list(input().strip())

cnt = 0

# k개 중에서 제일 큰거만 남기기

ans = []
que = deque(num)

while cnt < k:
    x = que.popleft()
    if ans:
        if ans[-1] > x:
            if x > que[0]:
                ans.append(x)
            else:
                cnt += 1
        elif ans[-1] == x:
            ans.append(x)
        else:
            while ans:
                if ans[-1] >= x or cnt >= k:
                    break
                ans.pop()
                cnt += 1
            ans.append(x)
    else:
        ans.append(x)

print(''.join(ans+list(que)))

# 이게 풀이 스택으로 해서 해결함
N, K = map(int, input().split())
num = list(input())
k = K
stack = []

for i in range(N):
    while(k > 0 and stack and stack[-1] < num[i]):
        stack.pop()
        k-=1
    stack.append(num[i])
    
print(''.join(stack[:N-K]))