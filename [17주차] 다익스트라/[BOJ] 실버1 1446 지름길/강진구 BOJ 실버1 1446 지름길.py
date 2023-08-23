import sys

input = sys.stdin.readline

n, d = map(int, input().split())

distance = [i for i in range(d+1)]

short = []

ans = 0

for _ in range(n):
    st,end,dist = map(int, input().split())
    if dist < end-st and end <= d:
        short.append((st,end,dist))

for i in range(d+1):
    distance[i] = min(distance[i], distance[i-1]+1)

    for s, e, shortcut in short:
        if i == s and e <= d and distance[i]+shortcut < distance[e]:
            distance[e] = distance[i]+shortcut

print(distance[d])