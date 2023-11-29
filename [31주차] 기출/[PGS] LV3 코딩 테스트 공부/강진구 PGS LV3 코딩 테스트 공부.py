# 이 문제 어려워서 답 보고 풀어봤습니다.

def solution(alp, cop, problems):
    max_alp, max_cop = 0, 0
    
    for problem in problems:
        max_alp = max(max_alp, problem[0])
        max_cop = max(max_cop, problem[1])
    
    alp = min(alp, max_alp)
    cop = min(cop, max_cop)
    
    dp = [[10e9]*(max_cop+1) for _ in range(max_alp+1)]
    dp[alp][cop] = 0 # i,j에 도달하는 최단시간
    for i in range(alp,max_alp+1): # 초기부터 제일 크게 만드는데까지
        for j in range(cop,max_cop+1):
            if i+1 <= max_alp:
                dp[i+1][j] = min(dp[i+1][j], dp[i][j]+1)
            if j+1 <= max_cop:
                dp[i][j+1] = min(dp[i][j+1], dp[i][j]+1)
            
            for a,b,c,d,e in problems:
                if i>=a and j>=b:
                    next_alp, next_cop = min(max_alp, i+c), min(max_cop,j+d)
                    dp[next_alp][next_cop] = min(dp[next_alp][next_cop], dp[i][j]+e)
                    
            
    
    return dp[-1][-1]