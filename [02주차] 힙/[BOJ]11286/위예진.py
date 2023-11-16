# N: 연산의 개수, x_list: 연산에 대한 정보 리스트
import sys
import heapq
input = sys.stdin.readline

N = int(input())
x_list = []    # 힙 생성

for _ in range(N):
    x = int(input())
    if x == 0:    # 힙에서 값 뽑아오기
        if x_list:    # 힙이 비어있지 않다면
            print(heapq.heappop(x_list)[1])
        else:    # 힙이 비어있으면 0 출력
            print(0)
    else:    # 힙에 값 넣기
        heapq.heappush(x_list, (abs(x), x))