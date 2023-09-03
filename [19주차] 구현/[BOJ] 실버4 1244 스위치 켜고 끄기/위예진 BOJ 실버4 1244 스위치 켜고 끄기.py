import sys
input = sys.stdin.readline

switch_num = int(input())    # 스위치의 수
switch_state = [False] + list(map(int, input().split()))    # 각 스위치의 상태 리스트
student_n = int(input())    # 학생 수

# 학생 정보 입력받으며 스위치 토글
for _ in range(student_n):
    g, n = map(int, input().split())    # 성별, 학생이 받은 수

    # 남학생: 자기가 받은 번호의 배수인 스위치를 토글
    if g == 1:
        for i in range(1, switch_num // n + 1):
            switch_state[i*n] = 1 - switch_state[i*n]
    # 여학생: 자기가 받은 수와 같은 번호가 붙은 스위치를 중심으로 좌우가 대칭인 구간까지의 스위치 상태 토글
    else:
        switch_state[n] = 1 - switch_state[n]    # 자기가 받은 스위치 토글
        for i in range(1, min(n - 1, switch_num - n) + 1):
            # 대칭이 아니면, 끝내기
            if switch_state[n-i] != switch_state[n+i]:
                break
        
            switch_state[n-i] = 1 - switch_state[n-i]
            switch_state[n+i] = 1 - switch_state[n+i]

# 출력은 하나씩 띄어쓰며, 20개씩 한 줄
for i in range(switch_num // 20 + 1):
    print(*switch_state[1+i*20:1+(i+1)*20])