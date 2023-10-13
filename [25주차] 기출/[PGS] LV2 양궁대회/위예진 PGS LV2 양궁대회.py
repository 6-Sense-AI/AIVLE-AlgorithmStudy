from itertools import product

def solution(n, info):
    ans = [-1]
    diff = 0
    info.reverse()
    
    for prod in product([True, False], repeat=11):
        ryan_n = sum(info[i] + 1 for i in range(11) if prod[i])
        if ryan_n <= n:
            ryan = sum(i for i in range(11) if prod[i])
            apeach = sum(i for i in range(11) if info[i] and not prod[i])
            if ryan - apeach > diff:
                diff = ryan - apeach
                ans = list(info[i] + 1 if prod[i] else 0 for i in range(11))
                ans[0] = n - ryan_n
    
    ans.reverse()
    
    return ans