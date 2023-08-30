# 1. 비어있는 칸 중에서 좋아하는 학생이 인접한 칸에 가장 많은 칸으로 자리를 정한다.
# 2. 1을 만족하는 칸이 여러 개이면, 인접한 칸 중에서 비어있는 칸이 가장 많은 칸으로 자리를 정한다.
# 3. 2를 만족하는 칸도 여러 개인 경우에는 행의 번호가 가장 작은 칸으로, 
#       그러한 칸도 여러 개이면 열의 번호가 가장 작은 칸으로 자리를 정한다.

import sys
input = sys.stdin.readline

n = int(input())
likes = [list(map(int, input().split())) for _ in range(n*n)]
room = [[False] * (n + 1) for _ in range(n + 1)]

# 첫번째 학생부터 가운데에 앉힘
i = n // 2 + n % 2 + 1
room[i][i] = likes[0][0]
# 이후 학생부터 조건을 고려하며 앉힘
for i in range(2, n * n + 1):
    s, l = likes[i-1][0], likes[i-1][1:]
    print(s, l)

print(likes)
print(room)