import sys
input = sys.stdin.readline

# dp 이중으로 선언하면 메모리 초과
# 재 선언 하는 방식으로 생성

n = int(input())
arr = list(map(int, input().split())) # 처음 세개

maxDP = arr
minDP = arr

for _ in range(n-1):
    arr = list(map(int, input().split()))
    # 세가지 값을 입력할 때 dp에 갱신
    maxDP = [arr[0] + max(maxDP[0], maxDP[1]), arr[1] + max(maxDP), arr[2] + max(maxDP[1], maxDP[2])]
    minDP = [arr[0] + min(minDP[0], minDP[1]), arr[1] + min(minDP), arr[2] + min(minDP[1], minDP[2])]

print(max(maxDP), min(minDP))