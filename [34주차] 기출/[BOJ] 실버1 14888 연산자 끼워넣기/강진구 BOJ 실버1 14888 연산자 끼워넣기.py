import sys

input = sys.stdin.readline

n = int(input())

n_lst = list(map(int, input().split()))

s_lst = list(map(int, input().split()))

max_value = -1e9
min_value = 1e9

# dfs로 풀기

def dfs(i, cur):
    global max_value, min_value

    if i == n:
        max_value = max(max_value,cur)
        min_value = min(min_value,cur)
    else:
        if s_lst[0]>0:
            s_lst[0] -= 1
            dfs(i+1,cur+n_lst[i])
            s_lst[0] += 1
        if s_lst[1]>0:
            s_lst[1] -= 1
            dfs(i+1,cur-n_lst[i])
            s_lst[1] += 1
        if s_lst[2]>0:
            s_lst[2] -= 1
            dfs(i+1,cur*n_lst[i])
            s_lst[2] += 1
        if s_lst[3]>0:
            s_lst[3] -= 1
            dfs(i+1,int(cur/n_lst[i]))
            s_lst[3] += 1

dfs(1,n_lst[0])

print(int(max_value))
print(int(min_value))