import sys
input = sys.stdin.readline

k, n = map(int,(input().split())) # 2*k 벨트갯수, 내구도 0개수
tmp = list(map(int, input().split()))
cb = [[0]*k for i in range(2)] # 컨베이어벨트
print(cb)
for i in range(2*k):
    if i < k:
        cb[0][i] = tmp[i]
    else :
        cb[1][-i+k-1] = tmp[i]

print(cb) # 컨베이어 생성

robot = [0]*k # 첫번쨰 줄만 보면 되니까

cnt = 1
while 1 :
    # 내구도가 0인 칸의 개수가 K개 이상이라면 과정을 종료한다.
    if cb.count(0) == n: break

    # 1. 벨트가 각 칸 위에 있는 로봇과 함께 한 칸 회전한다.
    # 1-1. 벨트 회전
    first = cb[1][0]
    for i in range(2*k-1,-1,-1):
            if i < k-1:
                cb[0][i+1] = cb[0][i]
            else :
                if i == 2*k-1 : continue
                else : cb[1][-i+k-1-1] = cb[1][-i+k-1]
    cb[0][0] = first
    print(cb)

    # 1-2. 로봇 회전
    # 가장 먼저 벨트에 올라간 로봇부터, 벨트가 회전하는 방향으로 한 칸 이동할 수 있다면 이동한다. 만약 이동할 수 없다면 가만히 있는다.
    # 로봇이 이동하기 위해서는 이동하려는 칸에 로봇이 없으며, 그 칸의 내구도가 1 이상 남아 있어야 한다.
    # if robot[i+1] == 0 and cb[i]

    # 올리는 위치에 있는 칸의 내구도가 0이 아니면 올리는 위치에 로봇을 올린다.
    if cb[0] != 0 and robot[0] == 0: # 내구성이 0이 아니고 인형이 없으면
        robot[0] = True # 인형을 올려줍니다.

    cnt += 1 # 그렇지 않다면 1번으로 돌아간다.

print(cnt)