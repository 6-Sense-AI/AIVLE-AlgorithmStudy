switch = int(input())  # 스위치 개수
state = list(map(int, input().split()))  # 스위치 상태
n = int(input())  # 학생 수

student = [
    list(map(int, input().split())) for _ in range(n)
]  # 학생 정보 (성별, 받은 숫자) # 남학생 = 1, 여학생 = 2


def boy(num, switch):  # 남학생일 경우
    n = num
    while n <= switch:
        if state[n - 1] == 1:
            state[n - 1] = 0

        else:
            state[n - 1] = 1

        n += num


def girl(num, switch):  # 여학생일 경우
    # 대칭인 부분이 없으면 자신만 바꾸므로 자신의 위치 넣은 상태로 시작
    s1 = num - 1  # 시작점
    s2 = num - 1  # 도착점
    i = 1

    while True:
        if num - 1 - i >= 0 and num - 1 + i < switch:  # 리스트 범위를 넘지 않으면
            if state[num - 1 - i] == state[num - 1 + i]:  # 대칭일 경우 시작점, 도착점 위치를 저장해준다
                s1 = num - 1 - i
                s2 = num - 1 + i
                i += 1

            else:
                break
        else:
            break

    if s1 == s2:  # 대칭인 경우가 없을 때,
        if state[s1] == 1:
            state[s1] = 0

        else:
            state[s1] = 1
    else:  # 대칭이 있을 때,
        for j in range(s1, s2 + 1):
            if state[j] == 1:
                state[j] = 0

            else:
                state[j] = 1


# 학생 정보를 돌면서 state 를 바꿔줌
for i in student:
    if i[0] == 1:
        boy(i[1], switch)
    else:
        girl(i[1], switch)

# 리스트 길이가 20 이상일 경우에 20개씩 잘라서 출력
if len(state) > 20:
    for i in range(0, len(state), 20):
        print(" ".join(map(str, state[i : i + 20])))

else:
    print(" ".join(map(str, state)))
