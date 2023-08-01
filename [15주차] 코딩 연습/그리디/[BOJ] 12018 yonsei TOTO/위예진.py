# 주어진 마일리지로 최대한 많은 과목을 신청 
# (내가 마일리지를 넣고 이후에 과목을 신청하는 사람은 없다) 
# 마일리지는 한 과목에 1에서 36까지 넣을 수 있다.
# (단 마일리지가 같다면 성준이에게 우선순위가 주어진다고 하자.)

import sys
input = sys.stdin.readline

# n: 과목수, m: 주어진 마일리지
n, m = map(int, input().split())

ms = []    # 해당 과목을 수강하기 위해 필요한 마일리지
for _ in range(n):

    # 입력받기
    _, p = map(int, input().split())    # 과목의 수강인원
    tmp = list(map(int, input().split()))    # 각 인원이 제출한 마일리지

    # 수강인원만큼 잘랐을 때, 가장 적은 마일리지 저장
    if len(tmp) >= p:    # 수강인원이 이미 찼다면,
        tmp.sort(reverse=True)    # 마일리지가 큰 순서대로 정렬
        ms.append(tmp[p - 1])    # 수강하는 사람 중 가장 적은 마일리지를 사용한 만큼 저장
    else:    # 수강인원이 차지 않았다면,
        ms.append(1)    # 마일리지 1만 저장
    
ms.sort()    # 필요한 마일리지가 적은 순서대로 정렬
res = 0    # 수강 가능한 과목수

for i in range(n):
    if m < ms[i]:    # 갖고 있는 마일리지가 턱없이 적으면, 종료
        break

    m -= ms[i]    # 필요한 마일리지만큼 사용
    res += 1    # 수강 과목 늘려주기

print(res)