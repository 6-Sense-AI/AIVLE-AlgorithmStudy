n = int(input())
m = int(input())  # 좌표를 알아낼 자연수
grp = [[0] * (n + 1) for _ in range(n + 1)]  # 달팽잉~, 1부터 시작하기 위해 n+1 해줌

# 뒤에서부터 시작했음. (n = 5라면 25부터 넣어줌)
# 이동 횟수가 n, n-1, n-1, n-2, n-2 ... 이런식으로 1이 될때까지 반복임
# n 인 경우에는 무조건 x좌표가 n번 증가함
# 이후에는 이동횟수(현재의 n)가 짝수일땐 횟수만큼 y좌표가 증가한 뒤, 다시 이동횟수만큼 x좌표가 감소함
# 홀수일땐 횟수만큼 y좌표 감소 뒤, x좌표 증가
# 이걸 25가 0이 될 때까지 반복해줬음

x = 0
y = 1
num = n**2

for _ in range(n):  # 이동 횟수가 n일 경우만 다르므로 미리 계산해줌
    x += 1
    grp[x][y] = num
    num -= 1

n -= 1

while num != 0:  # 이후는 이동횟수가 홀수, 짝수일 때 나눠서 num이 0이 될 때까지 반복해줌
    if n % 2 == 0:
        for i in range(n * 2):  # 같은 횟수를 두번 순서대로 돌아야 하므로 *2
            if i < n:  # 초반 n번 돌 때, y만 n번 증가
                y += 1
                grp[x][y] = num
                num -= 1

            elif i >= n:  # 두번째 n번 돌 때, x만 n번 감소
                x -= 1
                grp[x][y] = num
                num -= 1
        n -= 1
    else:
        for i in range(n * 2):
            if i < n:
                y -= 1
                grp[x][y] = num
                num -= 1

            elif i >= n:
                x += 1
                grp[x][y] = num
                num -= 1

        n -= 1

mx = 0  # m의 x좌표
my = 0  # m의 y좌표

for i in range(1, len(grp)):
    for j in range(1, len(grp)):
        print(grp[i][j], end=" ")
        if grp[i][j] == m:  # 출력하면서 m위치 검사도 같이 해줌
            mx = i
            my = j

    print()

print(mx, my, end=" ")
