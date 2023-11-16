n = int(input()) ## 전체 잔 개수
wines = [0]+[int(input()) for _ in range(n)] ## 첫 잔 선택 포함하기

d = [[0]*3 for _ in range(n+1)] ## [0,0,0] 으로 초기화

## d[a][b] : a번째 잔까지 b번 연속으로 마신다

d[1][1] = wines[1] ## 첫 잔으로 초기화

for i in range(2, n+1):
    d[i][0] = max(d[i-1][0], d[i-1][1], d[i-1][2])  ## i번째 안 마실 때 최대 포도주
    d[i][1] = d[i-1][0] + wines[i] ## i번째 마시는데 i-1번째 안 마셨을 때 최대 포도주 
    d[i][2] = d[i-1][1] + wines[i] ## i번째 마시는데 i-1번째 마셨을 때 최대 포도주
    
print(max(d[n]))

