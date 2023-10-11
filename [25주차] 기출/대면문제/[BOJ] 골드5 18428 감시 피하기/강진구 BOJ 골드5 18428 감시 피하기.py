import sys

input = sys.stdin.readline

n = int(input())

graph = [input().split() for _ in range(n)]

# graph에서 장애물 위치를 직접 바꿔주고 다 만족하는지 세야할듯

student = []
teacher = []
for i in range(n):
    for j in range(n):
        if graph[i][j] == 'T':
            teacher.append((i,j))
        elif graph[i][j] == 'S':
            student.append((i,j))

cnt = 0
for t in teacher:
    for s in student:
        if t[0]==s[0]:
            cnt += 1
# for t in teacher:
#     row,col = t
#     if 'S' in graph[row]:
#         for s in student:
#             if row == s[0]:
#                 min_c = min(col,s[1])
#                 max_c = max(col,s[1])
#                 for idx in range(min_c,max_c):
#                     if graph[row][idx] == 'X':
#                         if 'T' in graph[:][idx]:
#                             graph[row][idx] = 'O'
#                             cnt += 1

#             if col == s[1]:
#                 min_r = min(row,s[0])
#                 max_r = max(row,s[0])
#                 if 'O' not in graph[:][col]:
#                     for idx in range(min_r,max_r):
#                         if graph[idx][col] == 'X':
#                             if 'T' in graph[idx][:]:
#                                 graph[idx][col] = 'O'
#                                 cnt += 1
                

print(graph)
if cnt <= 3:
    print('YES')
else:
    print('NO')