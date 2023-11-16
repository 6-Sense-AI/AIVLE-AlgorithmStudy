import sys
input = sys.stdin.readline

X = int(input())
i = 64 # 64
cnt = 0 # 갯수
n = 0 # 64가 되기 위함

while i > 0 :
    if i > X: # x보다 크면 2로 나눔
        i//=2
        continue
    else : #작은 경우
        if n == X: # 같으면 끝
            break
        elif n+i>X: # n+i의 합이 X를 넘지 않으면
            i//=2
        else :
            n += i # 더해줌
            cnt += 1 # 카운트
            i//=2
print(cnt)
