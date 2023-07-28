n = int(input())

tree = map(int, input().split())

ans = 1

s_tree = sorted(tree, reverse=True)

for i,t in enumerate(s_tree):
    ans = max(i+1+t, ans)

print(ans+1)
