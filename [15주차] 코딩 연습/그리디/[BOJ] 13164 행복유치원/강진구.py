# 바로 옆에 애들끼리 비교해서 전체에서 큰걸 빼준다는 생각입니다

n, k = map(int, input().split())

child = list(map(int, input().split()))

def compare(lst):
    x = 0
    idx_lst = []
    for i, l in enumerate(lst):
        if i == 0:
            x = l
            continue
        else:
            c = (l - x)
            idx_lst.append((i, c))
            x = l
        
    return idx_lst

idx = compare(child)

sort_idx = sorted(idx, key = lambda x : -x[1])

cost = child[-1] - child[0]
for _,c in sort_idx[:k-1]:
    cost -= c

print(cost)
