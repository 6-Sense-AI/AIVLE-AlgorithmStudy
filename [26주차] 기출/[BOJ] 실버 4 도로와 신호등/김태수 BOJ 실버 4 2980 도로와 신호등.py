import sys
input =sys.stdin.readline

n, l = map(int,input().split())

now = 0
time = 0
for _ in range(n):
    d, r, g = map(int,input().split())
    
    time += (d-now)
    now = d
    if time % (r+g) <= r:
        time += (r-(time%(r+g)))

time += (l-now)
print(time)