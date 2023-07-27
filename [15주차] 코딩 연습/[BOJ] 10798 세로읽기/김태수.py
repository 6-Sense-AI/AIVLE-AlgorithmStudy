import sys
input = sys.stdin.readline

graph = [input().strip() for _ in range(5)]

max = len(graph[0])
for i in range(1, 5):
    com = len(graph[i])
    if com >= max:
        max = com

# print(max)
for i in range(max):
    for j in range(5):
        if i < len(graph[j]):
            print(graph[j][i], end="")
