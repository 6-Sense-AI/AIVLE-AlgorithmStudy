
def solution(n, info):

    from itertools import combinations

    answer = []
    
    # 낮은 점수부터
    # info.reverse()

    # 라이언 점수 case
    stack = []
    stack.append(info)
    print(stack)

    scores = [i for i in range(10,-1,-1)]
    while stack:
        
        case = stack.pop()
        
        print("case : ",case)

        # i = 1 , 한 점수에만 올인
        for i in range(1,n+1):
            comb = list(combinations(scores,i))
            
            tmp = []
            cnt = n
            for j in range(len(comb)):
                print("comb[j] : ",comb[j])
                for k in range(i):
                    while cnt>0 :
                        tmp.append(case[10-comb[j][k]]+1)
                        cnt -= case[10-comb[j][k]]+1
                    stack.append(tmp)

        print(stack)
    
    return answer
