from collections import deque
def check(u):
    word = []
    que = deque(u)
    i = 0
    while i<len(u):
        if que[0] == ')':
            if word and word[-1] == '(':
                word.pop()
                que.popleft()
            else:
                break
        else:
            word.append(que.popleft())
        i+=1
    if que:
        return False
    else:
        return True

# 재귀 함수 부분 다시 생각하기
# 개수를 세서 같아지는 지점까지 u,v를 나눔
def recurse(p):
    if p == '':
        return p
    else:
        u,v = '',''
        l_num,r_num = 0,0
        i = 0
        for p_ in p:
            if l_num == 0 or l_num!=r_num:
                u += p_
                if p_ == '(':
                    l_num += 1
                else:
                    r_num += 1
            else:
                v+=p_
        if check(u) == True:
            return u + recurse(v)
        else:
            w = '('+recurse(v)+')'
            u = u[1:-1]
            for i in u:
                if i == '(':
                    w += ')'
                else:
                    w += '('
            return w
        
def solution(p):
    answer = ''
    if check(p) == True:
        answer += p
    else:
        answer += recurse(p)
    
    
    return answer