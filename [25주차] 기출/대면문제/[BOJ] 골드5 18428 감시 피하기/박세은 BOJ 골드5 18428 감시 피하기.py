from collections import deque

n = int(input())
grp = [list(input().split()) for _ in range(n)]
t_index = [] # 선생님들 위치 리스트

for i in range(n): # 선생님들 위치값 저장
    for j in range(n):
        if grp[i][j] == 'T':
            t_index.append((i, j))

cnt = 0 # 장애물 수 count

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

tq = deque(t_index)

while tq:
    qx, qy = tq.popleft()

    for i in range(4):
        nx = qx + dx[i]
        ny = qy + dy[i]

        # 조건에 맞으면 검사중인 방향을 계속 검사하기 위해 while문 사용
        while True:
            # 좌표 범위가 리스트 범위를 넘지 않으면
            if nx >= 0 and nx < n and ny >= 0 and ny < n: 
                if grp[nx][ny] == 'S': # 이동한 곳에 학생이 있다면
                    if grp[nx-(dx[i])][ny-(dy[i])] == 'X': # 그리고 이동하기 직전에 있던 위치가 빈 공간이라면
                        grp[nx-(dx[i])][ny-(dy[i])] = 'O' # 장애물 채워주기
                        cnt += 1
                        break # 반복문 탈출해서 다른 방향 검사하기
                    
                    elif grp[nx-(dx[i])][ny-(dy[i])] == 'T': # 만약 이동하기 직전에 있던 위치에 선생님이 있다면
                        print('NO') # 이 학생은 무조건 걸릴 수 밖에 없으므로 'NO' 출력하고 
                        exit() # 코드 종료
                
                elif grp[nx][ny] == 'X': # 이동한 곳이 빈 공간이라면
                    # 현재 진행중인 방향으로 계속 가기
                    nx += dx[i] 
                    ny += dy[i]
                
                elif grp[nx][ny] == 'O': # 이동한 곳이 장애물이라면
                    break # 다른 방향 검사를 위해 반복문 탈출

                elif grp[nx][ny] == 'T': # 이동한 곳이 선생님이라면
                    # 현재 진행중인 방향으로 계속 가기
                    nx += dx[i]
                    ny += dy[i]
            
            else: # 좌표 범위가 리스트 범위를 벗어나면 반복문 탈출
                break

if cnt <= 3:
    print('YES')

else:
    print('NO')









    



