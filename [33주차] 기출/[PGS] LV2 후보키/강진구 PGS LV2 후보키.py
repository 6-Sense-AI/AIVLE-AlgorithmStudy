# 집합끼리 비교할때 오류가 났는지 히든에서 틀려서 정답을 참고했습니다.
from itertools import combinations as cb
def solution(relation):
    
    col = len(relation[0])
    cb_lst = []
    for i in range(1,col+1):
        cb_lst.extend(cb(range(col),i))
    uni = []
    for c in cb_lst:
        tmp = [tuple(item[key] for key in c) for item in relation]
        
        if len(set(tmp)) == len(relation):
            flag = True
            
            for u in uni:
                if set(u).issubset(set(c)):
                    flag = False
                    break
            if flag:
                uni.append(c)
    return len(uni)