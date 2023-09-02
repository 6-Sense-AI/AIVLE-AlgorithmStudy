
## 블로그 참고



## 자연수 입력

n = int(input())

## 타겟 입력

target = int(input())


## 달팽이 초기화

arr = [[0 for _ in range(n)] for _ in range(n)]

## 달팽이는 위 오른쪽 아래 왼쪽으로 이동
dx = [0, 1, 0, -1]
dy = [-1, 0, 1, 0]



direction = 0

## 현재 숫자
cnt = 1

## 달팽이 횟수
snail = 1

## 달팽이 가운데에서 시작
x, y = n // 2, n // 2
ans_y, ans_x = 0, 0

## n 제곱 만큼 진행
while cnt <= n ** 2:
    for _ in range(2):
        for _ in range(snail):
            if cnt <= n ** 2:

                ## 1부터 집어넣기
                arr[y][x] = cnt
                x += dx[direction]
                y += dy[direction]
                cnt += 1
        direction = (direction + 1) % 4
    snail += 1

for i in range(n):
    for j in range(n):
        print(arr[i][j], end=' ')
        if arr[i][j] == target:
            ans_y = i
            ans_x = j
    print()
print(ans_y + 1, ans_x + 1)
