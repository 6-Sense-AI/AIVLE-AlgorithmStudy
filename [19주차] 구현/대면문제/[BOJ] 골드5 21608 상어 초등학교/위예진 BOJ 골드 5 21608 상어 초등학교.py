# 1. 비어있는 칸 중에서 좋아하는 학생이 인접한 칸에 가장 많은 칸으로 자리를 정한다.
# 2. 1을 만족하는 칸이 여러 개이면, 인접한 칸 중에서 비어있는 칸이 가장 많은 칸으로 자리를 정한다.
# 3. 2를 만족하는 칸도 여러 개인 경우에는 행의 번호가 가장 작은 칸으로, 
#       그러한 칸도 여러 개이면 열의 번호가 가장 작은 칸으로 자리를 정한다.

import sys
input = sys.stdin.readline

# 입력 받기
n = int(input())    # n: 교실 한 면의 크기
likes = dict()    # likes: 좋아하는 학생 정보
for _ in range(n * n):
    tmp = list(map(int, input().split()))
    likes[tmp[0]] = tmp[1:]

room = [[False] * n for _ in range(n)]    # 교실 정보
moves = [(-1, 0), (1, 0), (0, -1), (0, 1)]    # 인접 방향

# 첫번째 학생부터 빈 칸에 앉힘
students = list(likes.keys())
room[1][1] = students[0]

# 인접영역에 좋아하는 학생 수 계산
def find_likes(now, r, c):
    score, empty = 0, 0
    l = likes[now]

    for mr, mc in moves:
        moveR, moveC = r + mr, c + mc
        if 0 <= moveR < n and 0 <= moveC < n:
            if not room[moveR][moveC]:
                empty += 1
                continue
            if room[moveR][moveC] in l:
                score += 1
    return score, empty

# 이후 학생부터 조건을 고려하며 앉힘
for stud in students[1:]:
    tmp = []

    # 모든 빈칸의 인접 좋아하는 학생 수, 빈 칸 수 구함
    for r in range(n):
        for c in range(n):
            if not room[r][c]:
                s, e = find_likes(stud, r, c)
                # [좋아하는 학생 수, 빈 칸 수, 행, 열]
                tmp.append([s, e, r, c])    
    
    # 조건에 맞게 정렬
    tmp.sort(key=lambda x: (-x[0], -x[1], x[2], x[3]))
    row, col = tmp[0][2], tmp[0][3]
    room[row][col] = stud


# 학생의 만족도 계산
ans = 0    # 학생 만족도 총합
for r in range(n):
    for c in range(n):
        # 인접 학생 수 계산
        score, _ = find_likes(room[r][c], r, c)

        # 만족도 계산
        if score:
            ans += 10 ** (score - 1)

print(ans)