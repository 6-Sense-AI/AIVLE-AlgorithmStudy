import sys
input = sys.stdin.readline

# 입력받기
num_pc = int(input())    # 컴퓨터의 수
num_node = int(input())    # 연결된 컴퓨터 쌍의 수
# 연결쌍의 정보리스트 (컴퓨터 번호는 1부터)
couple_info = [[] for _ in range(num_pc + 1)]    
for _ in range(num_node):
    pc1, pc2 = map(int, input().split())
    couple_info[pc1].append(pc2)
    couple_info[pc2].append(pc1)

# 바이러스에 걸린 pc의 수를 계산하는 함수
# dfs(재귀)로 구현
def search_virus_pc(now, visited):
    global num_virus_pc

    # 현재 노드 방문 처리
    visited[now] = True
    num_virus_pc += 1

    # 연결된 모든 노드 확인
    for i in couple_info[now]:
        if not visited[i]:    # 방문한 적이 없다면, 방문하기
            search_virus_pc(i, visited)

num_virus_pc = 0    # 바이러스에 걸린 pc의 수
visited = [False] * (num_pc + 1)    # 방문 여부 리스트

# 바이러스 pc 확인 및 결과출력
search_virus_pc(1, visited)
print(num_virus_pc - 1)    # 1번 컴퓨터 제외