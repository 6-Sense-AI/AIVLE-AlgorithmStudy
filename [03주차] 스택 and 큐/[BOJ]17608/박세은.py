stack =  []
n = int(input())
    
for _ in range(n):
    s = int(input())
    stack.append(s)

x = stack[-1]

for i in range(n-1, 0, -1):
    if  x >= stack[i] :
        stack.pop()

print(len(stack))
