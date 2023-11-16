import sys
input = sys.stdin.readline

stack = []
a = int(input())

for i in range(0, a):
    n = int(input())
    stack.append(n)
    
cnt = 0
for i in range(0, len(stack)-1):
    if stack[i] > stack[i+1]:
        cnt+=1

print(cnt)
