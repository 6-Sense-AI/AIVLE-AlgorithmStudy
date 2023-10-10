from collections import deque

def solution(queue1, queue2):
    sum1, sum2 = sum(queue1), sum(queue2)
    queue1, queue2 = deque(queue1), deque(queue2)
    
    answer = 0
    while answer < 2*(len(queue1)+len(queue2)):
        if sum1 == sum2:
            return answer
        
        if sum1 > sum2 and queue1:
            x = queue1.popleft()
            sum1, sum2 = sum1-x, sum2+x
            queue2.append(x)
        elif sum1 < sum2 and queue2:
            x = queue2.popleft()
            sum1, sum2 = sum1+x, sum2-x
            queue1.append(x)
        answer += 1
    
    return -1