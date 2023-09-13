from itertools import *

n = int(input())
arr = list(map(int, input().split()))

mt = ['+', '-', '*', '//']
mt_int = list(map(int, input().split()))
mt_str = []

i = 0
while i != 4:
    if mt_int[i] != 0:
        for _ in range(mt_int[i]):
            mt_str.append(mt[i])
        i += 1

    else:
        i += 1 

mt_str_all = list(permutations(mt_str, len(mt_str)))

ans = arr[0]

for i in range(n-1):
    if mt_str[i] == '+':
        ans += arr[i+1]
    
    elif mt_str[i] == '-':
        ans -= arr[i+1]
    
    elif mt_str[i] == '*':
        ans *= arr[i+1]
    
    else:
        ans //= arr[i+1]

mx = ans
mn = ans

for i in range(1, len(mt_str_all)):
    ans = arr[0]
    for j in mt_str_all[i]:
        for z in range(1, n):
            if j == '+':
                ans += arr[z]
        
            elif j == '-':
                ans -= arr[z]
            
            elif j == '*':
                ans *= arr[z]
            
            else:
                ans //= arr[z]
        
    if ans > mx:
        mx = ans
    
    if ans < mn:
        mn = ans

print(mx, mn)










