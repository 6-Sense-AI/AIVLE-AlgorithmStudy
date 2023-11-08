# 아직 못품...
from collections import deque
def solution(expression):
    answer = 0
    exp = []
    n = ''
    for e in expression:
        if e.isdigit():
            n+=e
        else:
            exp.append(int(n))
            exp.append(e)
            n = ''
    exp.append(int(n))
    i = 0
    que = deque(exp)
    while que:
        x = que.popleft()
        if x == '*':
            num = que[-1]*que[0]
            que.pop()
            que.popleft()
            que.append(num)
        else:
            if '*' in que:
                que.append(x)
            else:
                if x == '+':
                    num = que[-1]+que[0]
                    que.pop()
                    que.popleft()
                    que.append(num)
                else:
                    if '+' in que:
                        que.append(x)
                    else:
                        if x == '-':
                            num = que[-1]-que[0]
                            que.pop()
                            que.popleft()
                            que.append(num)
                        else:
                            if '-' in que:
                                que.append(x)
                            else:
                                answer = max(answer,abs(x))
        
    
    return answer