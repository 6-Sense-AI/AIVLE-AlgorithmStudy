from collections import deque
def solution(people, limit):
    # 무게 제한 > 최대몸무게
    # 무거운 사람 구출하되 가장 가벼운 사람 순으로 빼내면 된다
    # 데큐 안쓰면 시초남
    
    answer = 0
    # p = deque(people)
    # p.sort()
    p = deque(sorted(people))
    
    while 1 :
        if not p : break # p없으면
        tmp = p.pop()
        # len넣어줘야딤
        if len(p) > 0 and tmp + p[0] <= limit: # 가벼운애 빼도 ㄱㅊ으면 빼
            p.popleft()
        answer +=1
    
    return answer