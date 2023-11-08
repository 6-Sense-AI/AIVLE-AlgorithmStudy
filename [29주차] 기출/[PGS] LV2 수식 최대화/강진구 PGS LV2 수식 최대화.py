# 아직 미완
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
    
    while i<6:
        que = deque(exp)
        if i == 0:
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
        elif i == 1:
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
                        if x == '-':
                            num = que[-1]-que[0]
                            que.pop()
                            que.popleft()
                            que.append(num)
                        else:
                            if '-' in que:
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
                                        answer = max(answer,abs(x))
        elif i == 2:
            while que:
                x = que.popleft()
                if x == '+':
                    num = que[-1]+que[0]
                    que.pop()
                    que.popleft()
                    que.append(num)
                else:
                    if '+' in que:
                        que.append(x)
                    else:
                        if x == '*':
                            num = que[-1]*que[0]
                            que.pop()
                            que.popleft()
                            que.append(num)
                        else:
                            if '*' in que:
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
        elif i == 3:
            while que:
                x = que.popleft()
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
                                if x == '*':
                                    num = que[-1]*que[0]
                                    que.pop()
                                    que.popleft()
                                    que.append(num)
                                else:
                                    if '*' in que:
                                        que.append(x)
                                    else:
                                        answer = max(answer,abs(x))
        elif i == 4:
            while que:
                x = que.popleft()
                if x == '-':
                    num = que[-1]-que[0]
                    que.pop()
                    que.popleft()
                    que.append(num)
                else:
                    if '-' in que:
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
                                if x == '*':
                                    num = que[-1]*que[0]
                                    que.pop()
                                    que.popleft()
                                    que.append(num)
                                else:
                                    if '*' in que:
                                        que.append(x)
                                    else:
                                        answer = max(answer,abs(x))
        elif i == 5:
            while que:
                x = que.popleft()
                if x == '-':
                    num = que[-1]-que[0]
                    que.pop()
                    que.popleft()
                    que.append(num)
                else:
                    if '-' in que:
                        que.append(x)
                    else:
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
                                        answer = max(answer,abs(x))
        i+=1
    return answer