from collections import deque
pop_lst = []
push_lst = [1]

n = int(input())

n_lst = deque([])
p_lst = ['+']
for _ in range(n):
    n_lst.append(int(input()))

ans_lst = n_lst.copy()
i = 2
while i < (2*n)+1:
    if n_lst:
        x = n_lst.popleft()
    else:
        break
    if push_lst:
        y = push_lst.pop()
    else:
        break
    
    if y == x:
        pop_lst.append(x)
        p_lst.append('-')
        i -= 1
    else:
        push_lst.append(y)
        if i < n+1:
            push_lst.append(i)    
            p_lst.append('+')
        n_lst.appendleft(x)
    
    i+=1

if pop_lst == list(ans_lst):
    for j,p in enumerate(p_lst):
        if j!=len(p_lst)-1:
            print(p)
        else:
            print(p, end='')
else:
    print('NO')
