# import sys

# input = sys.stdin.readline

# n, k = map(int, input().split())

# arr = [0]*1000000

# point = []
# for _ in range(n):
#     ice, x = map(int, input().split())
#     arr[x] = ice
#     point.append(x)
    
# max_ice = 0

# for p in range(max(point)+1):
#     s = sum(arr[p:p+2*k+1])
#     max_ice = max(max_ice,s)

# print(max_ice)

import sys

n, k = map(int, sys.stdin.readline().split(" "))

# 양동이의 좌표별 얼음의 양
ice = [0] * 1000001

# 마지막 양동이의 위치
last_idx = 0

# 양동이의 얼음 양과 위치 저장
for _ in range(n):
    value, index = map(int, sys.stdin.readline().split(" "))
    ice[index] = value

    # 마지막 양동이의 위치 저장
    last_idx = max(last_idx, index)

# 윈도우 범위
size = (2*k) + 1

# 윈도우 범위 내의 합 초기화
window = sum(ice[:size])

# 윈도우 범위 내의 최댓값 저장
answer = window

# end는 윈도우의 마지막 위치를 의미합니다.
for end in range(size, last_idx+1):

    # 윈도우의 맨 뒤에 추가되는 값은 윈도우의 합에 더하고
    # 윈도우의 맨 앞에 있었던 값은 윈도우의 합에서 빼줍니다.
    window += ice[end] - ice[end-size]
    answer = max(answer, window)

print(answer)