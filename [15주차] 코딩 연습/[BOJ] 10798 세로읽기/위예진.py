import sys
input = sys.stdin.readline

nlist = []
for _ in range(5):
    tmp = input().rstrip()
    nlist.append(tmp + ' ' * (15 - len(tmp)))

res = ''    # 결과 문자열
for i in range(15):
    for l in range(5):
        if nlist[l][i] == ' ':
            continue
        res += nlist[l][i]

print(res)