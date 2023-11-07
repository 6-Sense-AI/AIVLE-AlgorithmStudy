import sys

input = sys.stdin.readline

n = int(input())

sig = [[] for _ in range(5)]
num = n//5
idx = 0

string = list(input().strip())

for i,s in enumerate(string):
    
    sig[idx].append(s)
    if (i+1)%num == 0:
        idx += 1

# 각 숫자를 확인하는 코드 짜기
zero = ['#','#','#','#','.','#','#','.','#','#','.','#','#','#','#']
two = ['#','#','#','.','.','#','#','#','#','#','.','.','#','#','#']
three = ['#','#','#','.','.','#','#','#','#','.','.','#','#','#','#']
four = ['#','.','#','#','.','#','#','#','#','.','.','#','.','.','#']
five = ['#','#','#','#','.','.','#','#','#','.','.','#','#','#','#']
six = ['#','#','#','#','.','.','#','#','#','#','.','#','#','#','#']
seven = ['#','#','#','.','.','#','.','.','#','.','.','#','.','.','#']
eight = ['#','#','#','#','.','#','#','#','#','#','.','#','#','#','#']
nine = ['#','#','#','#','.','#','#','#','#','.','.','#','#','#','#']

ans = ''

idx = 0
while idx < num:
    if sig[0][idx] == '#':
        number = []
        for s in sig:
            if idx+3<num:
                number.extend(s[idx:idx+3])
            else:
                number.extend(s[idx:])
        if number == zero:
            ans += '0'
        elif number == two:
            ans += '2'
        elif number == three:
            ans += '3'
        elif number == four:
            ans += '4'
        elif number == five:
            ans += '5'
        elif number == six:
            ans += '6'
        elif number == seven:
            ans += '7'
        elif number == eight:
            ans += '8'
        elif number == nine:
            ans += '9'
        else:    
            ans += '1'
            idx += 1
            continue
        idx += 2
    
    idx += 1

print(ans)