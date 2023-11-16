import sys
input = sys.stdin.readline
cnt = 0
a = int(input())

while a!=0:
    if a%2==1:
        cnt+=1
    a = a>>1
    #a = a//2

print(cnt)

23 
23/2 = 11 .. 1
11/2 = 5 .. 1
5 / 2 = 2 .. 1
2/ 2 =  0
