## 숫자를 더하거나 빼기

## 방법의 수 리턴
from collections import deque



def solution(numbers, target):
    ## 방법 수 초기화
    answer = 0

    ## 순서는 바꾸지 않으므로 첫 번째 노드는 리스트의 0번째 요소

    start = numbers[0]

    num_len = len(numbers)

    queue = deque()

    ## 더하기 빼기 둘 다 queue에 넣어주기
    queue.append([start,0])
    queue.append([(-1)*start, 0])

    while queue:
        trial, cal_num = queue.popleft()
        cal_num+=1

        ## 전체 숫자를 모두 활용하므로 연산 횟수와 리스트 길이를 비교

        ## 현재 연산값에 더하거나 뺀 거를 추가
        
        if cal_num < num_len:
            queue.append([trial+numbers[cal_num], cal_num])
            queue.append([trial-numbers[cal_num], cal_num])

        ## 연산 횟수 = 리스트 길이일 경우

        else:
            if trial == target:
                answer+=1
    return answer
            

