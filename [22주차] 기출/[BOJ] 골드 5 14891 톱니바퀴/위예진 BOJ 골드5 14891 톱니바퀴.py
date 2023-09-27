# 톱니바퀴 정보 (0: N극, 1: S극)
n = 4    # 톱니바퀴의 수
wheels = list(list(map(int, input())) for _ in range(n))
k = int(input())    # 회전 횟수
# 회전 방법 (번호, 방향) - (1: 시계 방향, -1: 반시계 방향)
rotations = list((map(int, input().split())) for _ in range(k))   
print(wheels)

# 지정한 방향으로 해당 바퀴를 회전시켜 반환하는 함수
def rotate_wheel(wheel, rotation):

    if rotation < 0:    # 반시계 방향 회전
        return wheel[1:] + wheel[0]
    else:    # 시계 방향 회전
        return wheel[-1] + wheel[:-1]
    
# 양쪽 톱니바퀴가 다른지 확인하는 함수
def check_diff(now, nxt):
    
    if now < nxt:    # 이웃 톱니바퀴가 오른쪽에 위치
        if wheels[now][2] != wheels[nxt][6]:
            return True
        
    if now > nxt:    # 이웃 톱니바퀴가 왼쪽에 위치
        if wheels[now][6] != wheels[nxt][2]:
            return True
        
    return False

for w, r in rotations:
    w -= 1
    new_rot = []    # 회전시킬 정보 리스트

    # 왼쪽 확인
    left = w - 1
    while left >= 0:
        if check_diff(w, left):
            new_rot.append((left, r * (-1)))
            left -= 1
        else:
            break
    # 오른쪽 확인
    right = w + 1
    while right < n:
        if check_diff(w, right):
            new_rot.append((right, r * (-1)))
            right += 1
        else:
            break

    # 회전시키기
    for n, rot in new_rot:
        wheels[n] = rotate_wheel(n, rot)

# 점수 계산
score = 0
for i in range(n):
    score += wheels[i][0] * (2 ** i)

print(score)