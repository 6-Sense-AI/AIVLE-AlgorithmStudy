# 나이트 반복 빼니까 맞았다!

n, m = map(int, input().split())
q = list(map(int, input().split()))  # 퀸
k = list(map(int, input().split()))  # 나이트
p = list(map(int, input().split()))  # 폰

ans = [[1 for _ in range(m)] for _ in range(n)]  # 안전한 위치 리스트 (초기엔 모두 1)
chess = [["n" for _ in range(m)] for _ in range(n)]  # 체스 위치 리스트 (빈 자리는 'n')

q_idx = []  # Q 좌표
k_idx = []  # K 좌표

for i in range(1, q[0] * 2, 2):
    chess[q[i] - 1][q[i + 1] - 1] = "q"  # 체스판에 퀸 배치해주기
    q_idx.append((q[i] - 1, q[i + 1] - 1))  # 퀸 좌표 저장
    ans[q[i] - 1][q[i + 1] - 1] = 0  # 퀸 위치 위험한 위치로 변경

for i in range(1, k[0] * 2, 2):
    chess[k[i] - 1][k[i + 1] - 1] = "k"  # 체스판에 나이트 배치해주기
    k_idx.append((k[i] - 1, k[i + 1] - 1))  # 나이트 좌표 저장
    ans[k[i] - 1][k[i + 1] - 1] = 0  # 나이트 위치 위험한 위치로 변경

for i in range(1, p[0] * 2, 2):
    chess[p[i] - 1][p[i + 1] - 1] = "p"  # 체스판에 폰 배치해주기
    ans[p[i] - 1][p[i + 1] - 1] = 0  # 폰 위치 위험한 위치로 변경

# 퀸 이동 규칙
q_step = [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (-1, 1), (1, -1), (1, 1)]

# 나이트 이동 규칙
k_step = [(-2, -1), (-2, 1), (-1, -2), (1, -2), (-1, 2), (1, 2), (2, -1), (2, 1)]

# Q
for q in q_idx:
    for s in q_step:
        # 이동 규칙만큼 움직이기
        nx = q[0] + s[0]
        ny = q[1] + s[1]

        while True:
            if nx < n and nx >= 0 and ny < m and ny >= 0:  # 범위를 넘지 않는다면
                if chess[nx][ny] == "n":  # 체스판 해당 위치가 비어있다면
                    ans[nx][ny] = 0  # 위험한 위치로 변경
                    # 이동 규칙만큼 더 움직이기
                    nx += s[0]
                    ny += s[1]

                else:
                    break  # 체스판에 장애물이 있다면 반복문 탈출

            else:
                break  # 이동 범위를 넘으면 반복문 탈출

# k
for k in k_idx:
    for s in k_step:
        nx = k[0] + s[0]
        ny = k[1] + s[1]

        if nx < n and nx >= 0 and ny < m and ny >= 0:
            ans[nx][ny] = 0

        else:
            continue

a = 0

for i in ans:  # 안전한 위치 총 합
    a += sum(i)

print(a)
