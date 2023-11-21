from collections import deque

def solution(people, limit):
    answer = 0
    
    # 리스트를 작은 수부터 오름차순으로 정렬
    people.sort()
    people = deque(people)
    
    # 리스트가 빌 때까지 반복
    while people:
        
        # 리스트에 요소가 하나뿐이라면
        if len(people) < 2:
            answer += 1
            people.pop()
            break
        
        # 리스트에 요소가 2개 이상이고,
        # 맨 앞, 맨 뒤의 요소의 합이 limit을 넘지 않는 경우
        if people[0] + people[-1] <= limit:
            answer += 1
            people.pop()
            people.popleft()
        else:
            answer += 1
            people.pop()
            
    return answer