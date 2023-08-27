

## 블로그 참고



## 스티커 2n개 구매

## n = 1이라면 두 스티커 중 큰 값

## n이 2면 대각선 합 중 큰 값

## 이전 합 중 큰 값의 대각선에 있는 값을 더한 것들끼리 비교해서 큰 값 반환

import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(2)]

    
    DP = [[0] * N for _ in range(2)]

    
    DP[0][0] = arr[0][0]
    DP[1][0] = arr[1][0]
    if N == 1:
        print(max(DP[0][0], DP[1][0]))
        continue

    
    DP[0][1] = arr[1][0] + arr[0][1]
    DP[1][1] = arr[0][0] + arr[1][1]
    if N == 2:
        print(max(DP[0][1], DP[1][1]))
        continue

    
    for i in range(2, N):
        
        DP[0][i] = max(DP[1][i-2], DP[1][i-1]) + arr[0][i]
        DP[1][i] = max(DP[0][i-2], DP[0][i-1]) + arr[1][i]
    
    

    print(max(DP[0][-1], DP[1][-1]))