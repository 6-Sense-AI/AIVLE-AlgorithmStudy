# 재귀사용하기 --> 메모리 초과..
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)

def all(x, y, total):
    if x == n:
        answer.append(total)
        return
    total += graph[x][y]

    if y == 0:
        all(x + 1, y, total)
        all(x + 1, y + 1, total)
    elif y == 1:
        all(x + 1, y - 1, total)
        all(x + 1, y, total)
        all(x + 1, y + 1, total)
    elif y == 2:
        all(x + 1, y - 1, total)
        all(x + 1, y, total)

n = int(input())
graph = []
for _ in range(n):
    graph.append(list(map(int, input().split())))

answer = []
for j in range(3):
    all(0, j, 0)

answer.sort()
a = len(answer)
print(answer)
print('{} {}'.format(answer[a-1], answer[0]))