# 이중 리스트로 dp를 만들어 봤는데 메모리 초과로 인해 찾아보니 받을 때마다 초기화 하는 방식으로 해결했습니다.
import sys

input = sys.stdin.readline

n = int(input())

board = list(map(int, input().split()))

dp_max = board
dp_min = board

for _ in range(1,n):
    a,b,c = map(int, input().split())
    dp_max = [a + max(dp_max[0], dp_max[1]), b + max(dp_max[0],dp_max[1],dp_max[2]), c + max(dp_max[1],dp_max[2])]
    dp_min = [a + min(dp_min[0], dp_min[1]), b + min(dp_min[0],dp_min[1],dp_min[2]), c + min(dp_min[1],dp_min[2])]

print(max(dp_max), min(dp_min))
