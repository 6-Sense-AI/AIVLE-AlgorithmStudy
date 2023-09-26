import sys
input = sys.stdin.readline

# 예제는 다 맞는데 10퍼에서 틀림

# 회전초밥
# 종류는 중복 가능
# 행사 1 : 벨트의 임의의 한 위치부터 k개의 접시를 연속해서 먹을 경우 할인된 가격 제공
# 행사 2 : 초밥의 종류 하나가 쓰인 쿠폰 발행, 1번 참가할 경우 초밥 하나를 무료 제공

# 답은 먹을수 있는 초밥 가짓수의 최댓값

# 접시 수, 초밥 가지 수, 연속해서 먹는 접시 수, 쿠폰 번호
n, d, k, c = map(int, input().split())

# 전략
# 배열의 크기가 이미 있으니 슬라이싱 윈도우였나 이거 사용
# 이때 추가 초밥을 정해야 하니까
from collections import deque # 데큐 써서 뺄거임

q = deque() # 최소 배열
belt = [int(input())for i in range(n)]

cnt = 0
ans = 0
max_ans = 0
for i in belt: # 벨트 돌려
    if len(q) < k : # q에 계속 추가
        if q.count(i) == 0 :
            cnt += 1
        q.append(i)
        if len(q) == k:
            if q.count(c) == 0: # 로또
                max_ans+=1
            max_ans += cnt

    else : #비교
        t = q.popleft() # 맨 앞의 값 삭제
        if q.count(t) == 0: cnt -= 1 # 이미 있었다면 1 빼줌

        if q.count(i) == 0: # 추가한 값이 q에 없으면
            cnt += 1 # 더하기

        q.append(i) # 값 추가
        ans = cnt
        if q.count(c) == 0:
            ans += 1
        if ans > max_ans:
            max_ans = ans # 최대

print(max_ans)