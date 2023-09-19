import sys
from itertools import combinations as cb, permutations as pm

input = sys.stdin.readline

n = int(input())

S = [list(map(int, input().split())) for _ in range(n)]

comb = list(cb(range(n), n//2))

i = 0
minv = 1e9

while i < len(comb)/2:
    p_lst1 = list(pm(comb[i], 2))
    p_lst2 = list(pm(comb[len(comb)-1-i],2))
    sum1 = 0
    for r,c in p_lst1:
        sum1 += S[r][c]
    
    sum2 = 0
    for r,c in p_lst2:
        sum2 += S[r][c]
    
    minv = min(minv, abs(sum1-sum2))
    i+=1

print(minv)