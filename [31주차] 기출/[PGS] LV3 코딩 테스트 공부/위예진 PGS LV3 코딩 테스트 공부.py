# 못 품,,

def solution(alp, cop, problems):
    ans = 0
    max_alp, max_cop = 0, 0
    min_alp, min_cop = 150, 150
    for a, c, _, _, _ in problems:
        max_alp, min_alp = max(a, max_alp), min(a, min_alp)
        max_cop, min_cop = max(c, max_cop), min(c, min_cop)
    
    # 아무 문제도 풀 수 없으면, 하나씩 올림
    if alp < min_alp:
        c = min_alp - alp
        alp += c
        ans += c    # 풀이 시간 추가
    if cop < min_cop:
        c = min_cop - cop
        cop += c
        ans += c    # 풀이 시간 추가
    
    # 모든 문제를 풀 수 있을 때까지 반복함
    while alp < max_alp or cop < max_cop:
        # 
        
    return ans