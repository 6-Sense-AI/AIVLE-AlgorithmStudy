import heapq
import sys
input = sys.stdin.readline

n = int(input())    # 연산의 개수
x_list = []    # 최대힙

for _ in range(n):
    x = int(input())
    if x > 0:
        heapq.heappush(x_list, -x)
    if x == 0:
        if x_list:
            print(-heapq.heappop(x_list))
        else:
            print(0)