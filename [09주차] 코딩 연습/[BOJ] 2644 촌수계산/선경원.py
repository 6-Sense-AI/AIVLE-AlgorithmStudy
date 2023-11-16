import sys

n = int(sys.stdin.readline()) ## 사람 수

a, b = map(int,sys.stdin.readline().split()) ## 촌수 계산 2명

m = int(sys.stdin.readline()) ## 관계의 개수

family = [[] for _ in range(n+1)] ## 가계도
visited = [False] * (n+1)

for i in range(m):
    x, y = map(int,sys.stdin.readline().split())  ## 관계 입력받기

    ## 가계도 완성
    family[y].append(x)
    family[x].append(y)
    

## 촌수 계산 리스트
result = []

#print(family)

def dfs(v, cnt):

    ## 시작지점 True
    cnt+=1
    visited[v] = True

    if v == b: ## 찾았으면 cnt append
        result.append(cnt)

    ## v 기준 모든 관계 확인시 종료
    for i in family[v]:
        if not visited[i]:
            dfs(i,cnt)

dfs(a, 0)

## 촌수 계산 못하면 -1
if len(result) == 0:
    print(-1)

else:
    print(result[0]-1)

