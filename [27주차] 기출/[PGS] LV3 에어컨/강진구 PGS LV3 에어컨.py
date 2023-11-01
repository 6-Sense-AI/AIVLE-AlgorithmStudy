from collections import deque
# 손님이 없을 때도 손님이 있는 시간을 고려해서 미리 맞춰 줘야함
# 계산할 때 시간을 따로 체크해서 원하는 시간에 원하는 온도로 맞춰주기
# 미완입니다.
def solution(temperature, t1, t2, a, b, onboard):
    answer = []
    board_time = deque([])
    for i,board in enumerate(onboard):
        if board == 1:
            board_time.append(i)
    for t in range(t1,t2):
        que = deque(onboard)
        tem = temperature
        cost = 0
        time = 0
        while que:
            c = que.popleft()
            if board_time and abs(board_time[0]-time) < tem-t:
                break
            else:
                if board_time and time == board_time[0]:
                    board_time.popleft()
                if c == 1:
                    if tem == t:
                        cost += b
                    else:
                        cost += a
                        if tem < t:
                            tem += 1
                        else:
                            tem -= 1
            time += 1
            
        answer.append(cost)
    return min(answer)