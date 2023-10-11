from collections import deque

def solution(queue1, queue2):
    answer = 1e9
    goal = sum(queue1 + queue2) / 2
    cnt = 0
    
    queue1 = deque(queue1)
    queue2 = deque(queue2)
    
    for i in range(len(queue1) + len(queue2)):
        s1 = sum(queue1)
        s2 = sum(queue2)
        
        if s1 == goal:
            answer = min(answer, cnt)
            break
            
        if s1 > s2:
            queue2.append(queue1.popleft())
            cnt += 1
        else:
            queue1.append(queue2.popleft())
            cnt += 1
            
    if answer == 1e9:
        answer = -1
    
    return answer