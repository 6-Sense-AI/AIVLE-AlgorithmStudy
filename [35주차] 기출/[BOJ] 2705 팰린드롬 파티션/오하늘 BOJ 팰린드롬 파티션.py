import sys

test = int(input()) # testcase
#try 1: 합분해 + 펠린드롬 체크

for _ in range(test) :
    def isP(n): # 팰린드롬 확인
        if n == n[::-1] :
            return True
        else : return False

    n = int(input()) # 수

    # 합분해 알고리즘 (DP)
    # dp = [[0] * i for i in range(n+1)]
    # dp[0][0] = 1
    # for i in range(n): # i
    #     for j in range
        

        
    print(isP(str(131)))