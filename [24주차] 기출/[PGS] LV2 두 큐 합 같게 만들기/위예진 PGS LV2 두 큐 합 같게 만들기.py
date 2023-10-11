from collections import deque

def solution(queue1, queue2):
    # 두 큐의 합이 2로 나누어떨어지지 않으면, -1 출력
    if sum(queue1 + queue2) % 2:
        return -1
    
    answer = -1    # 변경 횟수
    goal = sum(queue1 + queue2) / 2    # 큐의 합이 같아질 목표 값
    cnt = 0    # 같아졌을 때, 변경 횟수
    
    # 큐로 변경해주기
    queue1 = deque(queue1)
    queue2 = deque(queue2)
    # 합 계산
    s1 = sum(queue1)
    s2 = sum(queue2)
    
    for _ in range((len(queue1) + len(queue2)) * 2):
        
        if s1 == goal:
            answer = cnt
            break
            
        # 합이 더 큰 큐의 요소를 꺼내 다른 큐에 넣기
        if s1 > s2:
            queue2.append(queue1.popleft())
            cnt += 1
            s1 -= queue2[-1]
            s2 += queue2[-1]
        else:
            queue1.append(queue2.popleft())
            cnt += 1
            s1 += queue1[-1]
            s2 -= queue1[-1]
    
    return answer