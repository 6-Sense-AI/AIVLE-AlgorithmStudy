import sys

lst = []

for i in range(5):
    word = sys.stdin.readline().strip()
    lst.append(word)

mx = 0

for j in lst:
    if len(j) > mx :
        mx = len(j)

ans = []

for a in lst:
    if len(a) < mx:
        for _ in range(mx - len(a)):
            a.append("!")

# for q in range(mx):
#     for w in range(5):
#         ans.append(lst[w][q])

print(ans)
