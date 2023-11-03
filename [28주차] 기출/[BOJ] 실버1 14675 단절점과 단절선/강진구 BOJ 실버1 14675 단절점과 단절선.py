# import sys
# from collections import defaultdict
# import copy

# input = sys.stdin.readline

# n = int(input())

# node = []
# graph = defaultdict(list)
# for _ in range(n-1):
#     a,b = map(int, input().split())
#     graph[a].append(b)
#     graph[b].append(a)
#     node.append([a,b])

# q = int(input())

# question = []

# for _ in range(q):
#     t,k = map(int, input().split())
#     question.append((t,k))

# def check_tree(graph,node,q):
#     visit = [False for _ in range(n)]
#     t,k = q
#     if t == 1:
#         for i in range(1,n):
#             if i == k:
#                 del graph[i]
#                 visit[i]=True
#             else:
#                 if k in graph[i]:
#                     graph[i].pop(graph[i].index(k))
#     else:
#         a,b = node[k-1]
#         graph[a].pop(graph[a].index(b))
#         graph[b].pop(graph[b].index(a))
#     cnt = 1
#     stack = [list(graph.keys())[0]]
#     visit[0] = True
#     while False in visit:
#         if stack:
#             v = stack.pop()
#             visit[v-1] = True
#         else:
#             cnt += 1
#             for i,vis in enumerate(visit):
#                 if vis == False:
#                     stack.append(i+1)

#         for g in graph[v]:
#             if visit[g-1] == False:
#                 stack.append(g)
            
    
#     return cnt

# for ques in question:
#     graph_ = copy.deepcopy(graph)
#     if check_tree(graph_,node,ques) == 2:
#         print('yes')
#     else:
#         print('no')
'''
처음에 한방법은 전부 다 돌면서 트리가 몇개 생기는지 체크하려 했는데 시간초과가 뜸
그래서 찾아보니 어차피 노드는 두개 연결된거 끊어지면 트리 두개 되고 단절선은 무조건이라 그렇게 코드 짜면 성공임
'''

import sys

input = sys.stdin.readline

n = int(input())

graph = {i : -1 for i in range(1,n+1)}

for _ in range(n-1):
    a,b = map(int, input().split())
    graph[a] += 1
    graph[b] += 1

q = int(input())

for _ in range(q):
    t,k = map(int, input().split())
    if t == 1:
        if graph[k] < 1:
            print('no')
        else:
            print('yes')
    else:
        print('yes')