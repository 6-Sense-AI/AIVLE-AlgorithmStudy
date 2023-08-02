import sys
input = sys.stdin.readline

n, m = map(int, input().split()) # 과목 수, 주어진 마일리지 
plst = [] # 신청인원, 수강인원 list
mlst = [] # 마일리지 현황 list

# 입력 받기
for _ in range(n):
    p, l = map(int, input().split())
    plst.append((p,l))

    mil = map(int, input().split())
    mlst.append(list(mil))

# 마일리지 현황 내림차순 정렬
for i in range(len(mlst)):
    mlst[i].sort(reverse = True)


u_mil = [] # 내가 사용한 마일리지 list
s_mil = 0 # 내가 사용한 마일리지 총 합

for j in range(n): 
    if len(mlst[j]) < plst[j][1]: # 신청인원이 수강인원보다 적으면 마일리지 1 사용 (얼마를 써도 수강 가능하기 때문)
        u_mil.append(1)

    else: # 아니라면 마지막 수강 가능자와 같은 마일리지 사용
        u_mil.append(mlst[j][plst[j][1] - 1])

u_mil.sort() # 최소값 구해야 하므로 오름차순 정렬

i = 0
cnt = 0 # 수강 가능 과목 개수

while i < len(u_mil) and s_mil <= m:
    s_mil += u_mil[i]

    if s_mil <= m: # 사용 마일리지가 사용가능 마일리지보다 크지 않은 지점까지 확인
        cnt += 1
        i += 1

print(cnt)
