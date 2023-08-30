# 아직 틀림
n = int(input())
s = n

for i in range(1, n):
    for j in range(1, s - i + 1):
        s += j

print((s * 2 + 1) % 9901)
