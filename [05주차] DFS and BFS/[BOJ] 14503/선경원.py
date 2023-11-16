n, m = map(int, input().split())
r, c, d = map(int, input().split())
room = [list(map(int, input().split())) for _ in range(n)]

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def dfs(x, y, direction):
    ## 현재 위치 청소
    if room[x][y] == 0:
        room[x][y] = 2

    ## 네 방향 모두 청소가 이미 되어있거나 벽인 경우
    if room[x+1][y] != 0 and room[x-1][y] != 0 and room[x][y+1] != 0 and room[x][y-1] != 0:
        ## 후진할 위치가 벽이면 종료
        if room[x-dx[direction]][y-dy[direction]] == 1:
            return
            
        ## 후진한 경우 1로 돌아가 dfs
        else:
            dfs(x-dx[direction], y-dy[direction], direction)
            return
            

    ## 왼쪽 방향 돌리기 : 3 다음에는 0으로 돌아야 한다
    ## 나머지로 바꾼 다음 인덱스로 활용
    ## 청소기 방향과 반대 방향을 딕셔너리로 만들어서 해 볼 수도 있겠다 근데 좀 귀찮을듯..?
    
    for i in range(4):
        direction = (direction + 3) % 4  
        nx, ny = x + dx[direction], y + dy[direction]
        
    
    ## 주변 4칸 중 청소되지 않은 칸이 있는 경우 dfs
    
        if room[nx][ny] == 0:
            dfs(nx, ny, direction) 
            
    ## 위 조건 다 뚫으면 종료
            return

## dfs 수행
dfs(r, c, d)

## room에서 2인 것만 세주면 된다!
count = 0
for i in range(n):
    for j in range(m):
        if room[i][j] == 2:
            count += 1
print(count)
