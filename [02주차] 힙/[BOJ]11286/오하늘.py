import heapq
heap = []
minuscount = 0

n = int(input())

for i in range(0,n):
    num = int(input())
    if num == 0:
        if len(heap) == 0: # 배열이 비어있는 경우
            print(0)
        else :
            print(heapq.heappop(heap)) # 최소값 출력
    else :
        if num < 0: # 음수인 경우
            minuscount += 1
            heapq.heappush(heap, -num)
        else : # 양수인 경우
            heapq.heappush(heap, num)
        
