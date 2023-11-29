# 못품,,,,DP 문제!
# 풀이 봤음!

def solution(alp, cop, problems):
    max_alp, max_cop = 0, 0
    for a, c, _, _, _ in problems:
        max_alp = max(a, max_alp)
        max_cop = max(c, max_cop)
    
    # 가장 작은 노력부터 시작해서 dp 채워야 하므로
    alp = min(max_alp, alp)
    cop = min(max_cop, cop)
    # 문제 안풀고 단순히 각 노력을 올리기만 했을 때의 최대값
    max_cost = 100 * (max_alp + max_cop)

    dp = [[max_cost + 1 for _ in range(max_cop + 1)] for _ in range(max_alp + 1)]
    dp[alp][cop] = 0

    # max_alp, max_cop까지 dp 리스트 채움
    for i in range(alp, max_alp + 1):
        for j in range(cop, max_cop + 1):
            if i + 1 <= max_alp:
                dp[i + 1][j] = min(dp[i + 1][j], dp[i][j] + 1)
            if j + 1 <= max_cop:
                dp[i][j + 1] = min(dp[i][j + 1], dp[i][j] + 1)
            
            for alp_req, cop_req, alp_rwd, cop_rwd, cost in problems:
                if i >= alp_req and j >= cop_req:
                    nxt_alp = min(max_alp, i + alp_rwd)
                    nxt_cop = min(max_cop, j + cop_rwd)
                    dp[nxt_alp][nxt_cop] = min(dp[nxt_alp][nxt_cop], dp[i][j] + cost)
     
    return dp[-1][-1]