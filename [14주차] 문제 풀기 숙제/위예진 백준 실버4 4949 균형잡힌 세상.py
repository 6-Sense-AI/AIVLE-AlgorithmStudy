import sys
input = sys.stdin.readline

ans = []
while True:
    sentence = input().rstrip()
    if sentence == ".":
        break
    
    check = 'yes'
    stack = []
    for s in sentence:
        
        if s in ('(', '['):
            stack.append(s)
        elif s == ')':
            if stack and stack[-1] == '(':
                stack.pop()
            else:
                stack.append(')')
                break
        elif s == ']':
            if stack and stack[-1] == '[':
                stack.pop()
            else:
                stack.append(']')
                break
            
    if len(stack) == 0:
        print('yes')
    else:
        print('no')