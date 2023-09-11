import sys
input = sys.stdin.readline

# 정수의 개수, 리스트
n = int(input())    
nlist = list(map(int, input().split()))
# 찾을 정수의 개수, 리스트
t = int(input())    
targets = list(map(int, input().split()))

nlist.sort()    # 수열 정렬

# 이분탐색 함수
def find_n(number):
    left, right = 0, n    # 끝 인덱스 포함 X
    
    while left < right:
        mid = (left + right) // 2
        if nlist[mid] == number:    # 답을 찾으면, 1 출력
            return 1
        elif nlist[mid] < number:
            left = mid + 1
        else:
            right = mid    # 끝 인덱스 포함 X

    return 0    # 끝까지 못 찾으면, 0 출력

for i in targets:    # 전체 정수들 순서대로 찾기
    print(find_n(i))

############################# 주의할 점! #############################
# right를 n으로 설정(끝 인덱스 포함 X)했기 때문에
# 반복문에서 left < right, right = mid로 설정해야 함
# 그래야 전체 수를 전부 순회하며 원하는 값 찾을 수 있음!