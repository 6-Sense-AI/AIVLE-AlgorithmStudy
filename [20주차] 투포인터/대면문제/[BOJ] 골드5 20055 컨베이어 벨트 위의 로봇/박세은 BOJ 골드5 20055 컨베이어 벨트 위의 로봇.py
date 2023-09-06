n, k = map(int, input().split())
dmg = list(map(int, input().split()))
robot = [0 for _ in range(n * 2)]

process = 1

while dmg.count(0) < k:
    # 1단계 - 회전하기, 종료지점 로봇 삭제하기
    a = dmg[-1]
    del dmg[-1]
    dmg.insert(0, a)

    b = robot[-1]
    del robot[-1]
    robot.insert(0, b)

    if robot[n] == 1:
        robot[n] = 0

    # 2단계 - 먼저 들어온 로봇부터 이동, 내구도 감소, 종료지점 로봇 삭제하기
    for i in range(n - 1, -1, -1):
        if i + 1 == n and robot[i] == 1 and dmg[i + 1] != 0 and robot[i + 1] == 0:
            robot[i] = 0
            dmg[i + 1] -= 1

        elif i + 1 < n and robot[i + 1] == 0 and dmg[i + 1] != 0 and robot[i] == 1:
            robot[i] = 0
            robot[i + 1] = 1
            dmg[i + 1] -= 1

        else:
            continue

    # 3단계 - 로봇 올리기, 내구도 감소
    if robot[0] == 0 and dmg[0] != 0:
        robot[0] = 1
        dmg[0] -= 1

    # 4단계 - 내구도 0인 칸 갯수 확인
    if dmg.count(0) < k:
        # process 증가 후 종료까지 반복
        process += 1


print(process)
