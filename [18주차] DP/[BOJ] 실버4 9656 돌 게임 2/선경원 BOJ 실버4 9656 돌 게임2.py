
## 돌은 1개 또는 3개
## 막돌이 패배

## 한 라운드를 돌면 남은 돌로 돌 게임을 다시 시작한다

n = int(input())

## n = 1일 경우 창영이의 승리

## n = 2일 경우 상근이 승리

## n = 3일 경우 창영 승리

if n % 2 == 1:
    print("CY")
else:
    print("SK")