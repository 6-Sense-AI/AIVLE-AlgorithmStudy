from collections import deque

def solution(queue1, queue2):
    qu_1 = deque(queue1)
    qu_2 = deque(queue2)
    sum_1 = sum(qu_1)
    sum_2 = sum(qu_2)

    for i in range(len(queue1) * 2):
        if sum_1 == sum_2:
            return i
        if sum_1 > sum_2:
            num = qu_1.popleft()
            qu_2.append(num)
            sum_1 -= num
            sum_2 += num
        else:
            num = qu_2.popleft()
            qu_1.append(num)
            sum_2 -= num
            sum_1 += num
    return -1