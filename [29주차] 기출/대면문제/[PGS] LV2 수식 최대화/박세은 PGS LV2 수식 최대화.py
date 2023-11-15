from itertools import *
from collections import deque
import copy

def solution(expression):
    eps = []
    num = []
    es = []
    
    for i in expression:
        if i == '*' or i == '-' or i == '+':
            if i not in eps:
                eps.append(i)
            num.append(' ')
        
        else:
            num.append(i)
                    
    eps = deque(permutations(eps, len(eps)))
    num = list(map(int, ''.join(num).split(' ')))
    
    mx = 0

    while eps:
        ep = eps.popleft()
        tst_num = deque(copy.deepcopy(num))
        tst_es = deque(copy.deepcopy(es))
        
        for e in ep:
            l = tst_num[-1]
            t = tst_es.popleft()
            n1 = tst_num.popleft()
            n2 = tst_num.popleft()
            
            if t == e:
                if t == '*':
                    tst_num.appendleft(n1 * n2)

                if t == '+':
                    tst_num.appendleft(n1 + n2)

                if t == '-':
                    tst_num.appendleft(n1 - n2)

            
            else:
                tst_es.insert(1, t)
                tst_num.insert(-1, n1)
                
                if n2 == l:
                    tst_num.insert(-1, n2)
                else:
                    tst_num.insert(0, n2)
