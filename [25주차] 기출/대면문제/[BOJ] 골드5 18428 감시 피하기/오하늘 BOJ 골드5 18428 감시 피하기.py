import sys
input = sys.stdin.readline

# 감시피하기
# 장애물 3개로 선생님의 눈을 피할 수 있는지 구하기
# T:선생님 S:학생 O:장애물

# 상, 하, 좌, 우
dx = [-1,1,0,0]
dy = [0,0,-1,1]

n = int(input())
# arr = [list(input().split()) for i in range(n)] # 배열

arr = []
s_list = [] # 학생 좌표
for i in range(n):
    temp = list(input().split())
    for j in range(len(temp)):
        if temp[j] =='S': s_list.append([i,j])
    arr.append(temp)

print(arr)
print(s_list)

# 전략 : 한명씩 순열 구해서 가장 min으로. -> 시간초과가 마음에 걸림..

from itertools import permutations

for i in range(len(s_list)):
    x, y = s_list[i]
    s_t = []
    if arr[x].count('T') > 0:
        for j in range(y+1,len(arr[x])):
            if arr[x][j] == 'T': break
            else : s_t.append([x,j])
    print(s_t)

# print(arr)