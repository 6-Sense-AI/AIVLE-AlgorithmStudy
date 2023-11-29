# 테케는 다 맞는데 제출하면 처음부터 틀림ㅠㅠ

import sys
input = sys.stdin.readline

n = int(input())
words = [list(input().rstrip()) for _ in range(n)]
n10 = ['' for _ in range(8)]    # 자릿수에 해당하는 알파벳
alp_num = dict()    # 알파벳 등장 횟수
alp_to_num = dict()    # 각 알파벳에 대응하는 숫자 사전

# 자릿수 배정
for w in words:
    for i in range(len(w)):
        alp = w[-(i+1)]

        if alp not in alp_num:    # 처음 등장
            alp_num[alp] = 1
        else:
            alp_num[alp] += 1
        n10[i] += alp

# 순서 배정 (자릿수, 등장 횟수 순으로)        
ord_alp = ''
for w in n10:
    if len(w) > 2:
        ord = []
        for alp in w:
            ord.append((alp_num[alp], alp))
        ord = sorted(ord, key=lambda x: x[0])
        for _, alp in ord:
            ord_alp += alp
    else:
        ord_alp += w
n10 = ''.join(n10)[::-1]

# 알파벳 대응 사전 채우기
ni = 9
for alp in ord_alp[::-1]:
    if not alp in alp_to_num:
        alp_to_num[alp] = ni
        ni -= 1

# 숫자 연산
ans = 0
for w in words:
    for i, alp in enumerate(w[::-1]):
        ans += (alp_to_num[alp] * (10 ** i))

print(ans)