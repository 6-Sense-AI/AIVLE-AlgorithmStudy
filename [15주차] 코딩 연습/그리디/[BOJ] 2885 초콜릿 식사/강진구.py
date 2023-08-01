import math

k = int(input())

for i in range(100):
    if (2**i) >= k:
        n = i
        break

s = 2**(n)
m = 0

while k > 0:
    if k % s == 0:
        break
    s /= 2
    m += 1

print(2**n, m)
