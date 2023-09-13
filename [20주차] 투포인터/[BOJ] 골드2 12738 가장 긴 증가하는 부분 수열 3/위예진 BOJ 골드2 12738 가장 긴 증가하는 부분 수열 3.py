# LIS + 이분탐색
# LIS 리스트를 만드는 과정에서 각 값들을 찾을 때, 이분탐색 활용

import sys
input = sys.stdin.readline

nl = int(input())    # 수열의 길이
nlist = list(map(int, input().split()))    # 수열
lis = [nlist[0]]    # 가장 긴 증가하는 부분 수열

def binary_search(target):
    # lis 리스트는 오름차순으로 정렬되어 있기 때문에 이분탐색 가능
    left, right = 0, len(lis)
    while left < right:
        mid = (left + right) // 2

        if lis[mid] == target:    # 해당 값 찾으면, 종료
            return mid
        elif lis[mid] < target:
            left = mid + 1
        else:
            right = mid

    # 못 찾고 끝났을 때, 해당 값이 right보다 작음 
    # -> 해당 값으로 갱신
    return right

for n in nlist[1:]:

    # lis 리스트의 가장 큰 수보다 크다면, 그대로 넣어주기
    if n > lis[-1]:    
        lis.append(n)
        continue
    
    # 아니라면, lis 리스트에서 i가 들어갈 자리 찾음 (이분탐색)
    lis[binary_search(n)] = n

print(len(lis))