import sys
import itertools
input = sys.stdin.readline

n = int(input())
arr = list(map(int,input().split()))
cal = list(map(int,input().split()))

# 결과값 저장을 위한 리스트
result = []

mm = []
for i in range(cal[0]):
    mm.append('+')
for i in range(cal[1]):
    mm.append('-')
for i in range(cal[2]):
    mm.append('*')
for i in range(cal[3]):
    mm.append('//')

# 순열로 연산자 정렬 후 리스트에 각각의 요소 하나씩 삽입하기
nPr = itertools.permutations(mm, sum(cal))
tmp = []
for i in nPr:
    tmp.append(list(i))
tmp2=[]
for i in tmp:
    tmp2.append(list(i))
# print(tmp2)
# print(len(tmp2))

# 노가다 on
for i in range(len(tmp2)):
    cnt = 0
    for j in range(n-1):
        if tmp2[j] == '+':
            cnt = cnt + arr[i] + arr[i+1]
        elif tmp2[j] == '-':
            cnt = cnt + arr[i] - arr[i+1]
        elif tmp2[j] == '*':
            cnt = cnt + arr[i] * arr[i+1]
        elif tmp2[j] == '//':
            if cnt < 0:
                cnt = abs(cnt)