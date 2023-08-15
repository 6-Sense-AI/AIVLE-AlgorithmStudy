# 재귀말고 BFS로 풀어보기
from collections import deque

def solution(numbers, target):
    count = 0
    queue = deque()
    queue.append((0,0))
    while queue:
        current_sum, index = queue.popleft()
        
        if index == len(numbers):
            if current_sum == target:
                count += 1
        else:
            current_number = numbers[index]
            queue.append((current_sum + current_number, index + 1))
            queue.append((current_sum - current_number, index + 1))
    return count