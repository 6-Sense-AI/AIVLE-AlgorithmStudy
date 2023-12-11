from itertools import combinations

def solution(relation):
    rows, cols = len(relation), len(relation[0])
    ckey = []
    
    # (1 ~ 컬럼 개수)만큼 칼럼 조합 고르기
    for n in range(1, cols + 1):
        for combi in combinations(range(cols), n):
            # 최소성 확인
            key = ['0'] * cols
            for c in combi:
                key[-(c + 1)] = '1'
            key = int(''.join(key), 2)
            check = True
            for c in ckey:
                if (key & c) == c: 
                    check = False
                    break
            if not check:
                continue
            
            # 유일성 확인
            tmp_keys = set()
            for r in range(rows):
                tmp = []
                for i in combi:
                    tmp.append(relation[r][i])
                tmp_keys.add(tuple(tmp))
            if len(tmp_keys) == rows:
                ckey.append(key)
    return len(ckey)