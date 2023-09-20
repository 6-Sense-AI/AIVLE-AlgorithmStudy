# 블록 추가되지 X, 최대 5번 이동시켜서 얻을 수 있는 가장 큰 블록 출력
from copy import deepcopy
import sys
input = sys.stdin.readline

n = int(input())    # 보드의 크기
game = [list(map(int, input().split())) for _ in range(n)]    # 게임판의 초기 상태
max_block = 0    # 만들어지는 가장 큰 블록 값 초기화

# 상하좌우로 이동시키는 함수
def move_blocks(graph, dir):
    # 1. 이동시켜줄 기준 인덱스 선정
    # 2. 이동할 값이 0이 아니라면, 아래 수행
    # 3. 이동할 값의 위치에 다음 블록이 이동할 수 있도록 값 복사하고, 0으로 초기화
    # 4. 기준인덱스가 0이면, 값 이동만
    # 5. 기준인덱스가 이동할 값과 같으면, 값 이동시키고 기준인덱스 변경
    # 6. 기준인덱스가 이동할 값과 같지 않다면, 처음에 복사한 값을 넣어줌

    if dir == 0:    # 상
        for col in range(n):
            top = 0
            for row in range(1, n):
                if graph[row][col]:
                    tmp = graph[row][col]
                    graph[row][col] = 0
                    if graph[top][col] == 0:
                        graph[top][col] = tmp
                    elif graph[top][col] == tmp:
                        graph[top][col] = tmp * 2
                        top += 1
                    else:
                        top += 1
                        graph[top][col] = tmp


    elif dir == 1:    # 하
        for col in range(n):
            top = n - 1
            for row in range(n - 2, -1, -1):
                if graph[row][col]:
                    tmp = graph[row][col]
                    graph[row][col] = 0
                    if graph[top][col] == 0:
                        graph[top][col] = tmp
                    elif graph[top][col] == tmp:
                        graph[top][col] = tmp * 2
                        top -= 1
                    else:
                        top -= 1
                        graph[top][col] = tmp

    elif dir == 2:    # 좌
        for row in range(n):
            top = 0
            for col in range(1, n):
                if graph[row][col]:
                    tmp = graph[row][col]
                    graph[row][col] = 0
                    if graph[row][top] == 0:
                        graph[row][top] = tmp
                    elif graph[row][top] == tmp:
                        graph[row][top] = tmp * 2
                        top += 1
                    else:
                        top += 1
                        graph[row][top] = tmp

    else:    # 우
        for row in range(n):
            top = n - 1
            for col in range(n - 2, -1, -1):
                if graph[row][col]:
                    tmp = graph[row][col]
                    graph[row][col] = 0
                    if graph[row][top] == 0:
                        graph[row][top] = tmp
                    elif graph[row][top] == tmp:
                        graph[row][top] = tmp * 2
                        top -= 1
                    else:
                        top -= 1
                        graph[row][top] = tmp

    # 이동한 결과 그래프 반환함
    return graph

# 최대 횟수 이하만큼 탐색하는 함수
def backtracking(graph, cnt):
    global max_block

    # 최대 이동 횟수에 도달하면,더 큰 값으로 갱신
    if cnt == 5:    
        max_block = max(max_block, max(sum(graph, [])))
        return
    
    # 더 이동할 수 있다면, 가능한 곳으로 이동시키기
    for dir in range(4):    # 상하좌우 이동
        # 이전 값이 기록돼 있어야 하므로, 깊은 복사로 복사해서 넘겨주기
        moved_graph = move_blocks(deepcopy(graph), dir)
        backtracking(moved_graph, cnt + 1)

backtracking(game, 0)
print(max_block)