# 연세 toto
# 신청한 사람 수 - 수강인원해서 나온 수 = 내가 고려할 사람의 수 = 마일리지 생각

import sys
input = sys.stdin.readline

n, m = map(int,input().split()) # 과목 수, 마일리지
sublist = []

for i in range(n):
    p, l = map(int, input().split()) # 신청한 사람 수, 수강인원
    temp = p - l + 1 # 성준이가 이겨야 할 사람 수

    # 신청한 사람 수 - 수강인원 > 0
    tmplist = list(map(int, input().split()))
    if temp > 0 :
        tmplist.sort() # 오름차순
        temp = tmplist[temp-1]
        sublist.append(temp)

    # 신청한 사람 수 - 수강인원 <= 0
    else :
        sublist.append(1)

sublist.sort() # 정렬

# 성준이가 고려할 마일리지
cnt = 0
for i in sublist:
    m-=i
    cnt+=1
    if m < 0:
        print(cnt-1)
        break
if m > 0:
        print(cnt)


## 의문 !!! 28줄부터 밑에 처럼 썼을때 62퍼에서 런타임에러(index error)가 떴다.. 왜일까...
cnt = 0
while 1:
    m = m-sublist[cnt]
    if m < 0 or cnt > n : break
    cnt += 1
