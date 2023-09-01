# 남학생 - 스위치 번호가 자기가 받은 수의 배수이면 스위치 상태변경
# 여학생 - 받은 수를 중심으로 좌우 대칭이면서 가장 많은 스위치를 포함하는 구간변경
import sys
input = sys.stdin.readline

# 입력받기
n = int(input())
num = list(map(int, input().split()))

# 인덱스를 맞추기 위해 0번 인덱스에 숫자추가
num.insert(0, 2)
stu = int(input())
for i in range(stu):
    a, b = map(int, input().split())
    # 남학생일 경우
    if a == 1:
        for i in range(b, n+1, b):
            if num[i] == 0:
                num[i] = 1
            elif num[i] == 1:
                num[i] = 0
    # 여학생일 경우
    elif a == 2:
        if num[b] == 1:
            num[b] = 0
        elif num[b] == 0:
            num[b] = 1
        for i in range(1, n//2):
            if (b-i <= 0) or (b+i > n):
                break
            if num[b-i]== num[b+i]:
                if num[b-i] == 0:
                    num[b-i] = 1
                    num[b+i] = 1
                elif num[b-i] == 1:
                    num[b-i] = 0
                    num[b+i] = 0
            elif num[b-i] != num[b+i]:
                break

# 처음에 추가했던 인덱스 0번 제거하기
num.remove(2)

# 한 줄에 20개씩 출력
for i in range(0, n):
    print(num[i], end = " ")
    if (i+1) % 20 == 0 :
        print()