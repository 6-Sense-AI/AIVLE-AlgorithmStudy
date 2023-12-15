from itertools import combinations, permutations
def solution(relation):
    answer = 0
    row = len(relation) # 행, row, 가로
    col = len(relation[0]) # 열, col, 세로
    
    combi = [] # 조합
    for i in range(1, col+1):
        # 일단 조합 다 때려 넣어
        combi.extend(combinations(range(col),i))
        # extend 는 append랑 다르다. append 는 추가면 expend 는 확장의 개념
        
    # 유일성
    unique = []
    for i in combi:
        tmp = [tuple([item[key] for key in i]) for item in relation]
        
        if len(set(tmp)) == row:
            unique.append(i) # 유일성
            
    
    # 최소성
    answer = set(unique)
    for i in range(len(unique)) :
        for j in range(i+1, len(unique)) :
            # 부분집합이 있다면
            if len(unique[i]) == len(set(unique[i])& set(unique[j])): answer.discard(unique[j])
            
            #discard를 쓰는이유는 없을때 에러가 안나고 무시하기 때문임 remove를 쓰면 에러가 남.
            
    return len(answer)

# 근데 저 26번줄 말고, issubset을 쓰는게 더 정확하다.
# set(unique[i].issubset(set(unique[j])))

   #유일성 이런식으루
    # unique = []
    # for i in combi:
    #     tmp = [tuple([item[key] for key in i]) for item in relation]

    #     if len(set(tmp)) == row:    # 유일성
    #         put = True
            
    #         for x in unique:
    #             if set(x).issubset(set(i)):  # 최소성
    #                 put = False
    #                 break
                    
    #         if put: unique.append(i)
   
    # return len(unique)