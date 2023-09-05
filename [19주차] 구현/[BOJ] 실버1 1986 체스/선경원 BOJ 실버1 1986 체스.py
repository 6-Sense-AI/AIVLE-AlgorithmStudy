

## 체스판 크기 입력

n, m = list(map(int, input().split()))

queen = list(map(int, input().split()))

knight = list(map(int,input().split()))

pawn = list(map(int, input().split()))


## 체스판 초기화

board = [[0]*n for i in range(n)]

## 중복 카운트를 피하기 위한 visited

visited = [[False]*n for i in range(n)]

## 공격예정 체스판

underattack = [[False]*n for i in range(n)]

## 폰은 장애물 역할만 수행
## 나이트, 퀸, 폰의 이동을 각자 나눠보자
## 공격이 가능한 영역, 현재 말이 있는 영역을 모두 True로 하고 False인 칸만 세어서 반환하자

## 나이트는 장애물과 무관하게 이동할 수 있다

def knight_move(r, c):

    dx = [2, 2, -2, -2]
    dy = [-1, 1, 1, -1]

    ## 체스판을 벗어나지 않거나 도착점에 다른 말이 없는 경우, 중복이 아닌 경우
    for i in range(4):
        nx = r + dx
        ny = c + dy

        if 0<=nx<n and 0<=ny<n and board[nx][ny]!= 0 and not visited[nx][ny]:
            underattack[nx][ny] = True
            visited[nx][ny] = True


def queen_move(r, c):

    dx = [0]*n
    dy = [0]*n
    
    for i in range(1, n+1):
        r += i
        c += i
        if board[r][c]==0:
            break
        elif 0<=r<n and 0<=c<n and board[r][c]!= 0 and not visited[r][c]: