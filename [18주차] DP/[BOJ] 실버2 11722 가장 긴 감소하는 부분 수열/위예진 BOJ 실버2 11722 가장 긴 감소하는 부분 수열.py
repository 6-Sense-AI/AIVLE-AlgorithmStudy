# 일정한 크기만큼 줄어드는 X, 앞이 뒤보다 크면 됨 O
# 각 위치에서 시작했을 때의 수열 길이를 모두 구하면 됨

import sys
input = sys.stdin.readline

na = int(input())    # 수열의 길이
alist = list(map(int, input().split()))    # 수열 리스트

# 각 위치에 도달했을 때의 최대 수열 길이(1로 초기화)
dp = [1 for _ in range(na)]

# 앞부터 차례대로 최대 수열 길이 계산
for i in range(1, na):    # 각 index 모두 방문
    for j in range(i):    # 각 index에 도달했을 때의 최대 수열 길이 계산
        if alist[i] < alist[j]:    # 앞의 수가 더 크면
            dp[i] = max(dp[i], dp[j] + 1)    # 자신보다 큰 값이면서, 순차적으로 찾아온 수열 값이 길다면 갱신

print(max(dp))    # 완성한 dp 리스트에서 최대 수열 길이가 가장 긴 값 출력