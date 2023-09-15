import sys
input = sys.stdin.readline

from itertools import combinations #조합

n = int(input())
arr = [list(map(int,input().split())) for i in range(n)]

# 전략 : 팀의 '조합'들 중 또 남은 팀들중의 2명 조합을 구하면 됨
# 내가 놓쳤던 부분 : 조합 두번 돌리려고 했는데 생각해보니 1,2,3이 골라지면 4,5,6가 강제임

team = [] #팀
for i in range(n):
    team.append(i)

ab = [] # 능력
ans = int(1e9)
for tt in combinations(team,n//2): # 조합
    start = 0
    link = 0
    for i in tt: # 스타트
        for j in tt:
            start+=arr[i][j]
    ex_start = [] # 스타트를 제외한 팀
    for i in range(n):
        if i not in tt: ex_start.append(i)

    for i in ex_start:
        for j in ex_start:
            link+=arr[i][j]

    if ans>abs(start-link) : # 차 중에 최소
        ans=abs(start-link)

print(ans)

