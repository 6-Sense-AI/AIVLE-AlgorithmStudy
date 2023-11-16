import heapq
import sys

n = int(sys.stdin.readline())
values_1 = []
values_2 = []
#cnt = 0
for i in range(0, n):
    num = int(sys.stdin.readline())
    values_1.append(num)
    values_2.append(num)

#for i in values:
#    if i == 0:
#        cnt += 1

heapq.heapify(values_2)

for i in values_1:
    if i == 0:
        if len(values_1) == 0: # 배열이 비었을 때
            print('0')
        else:                  # 배열에 값이 있을 때
            print(heapq.heappop(values_2))
