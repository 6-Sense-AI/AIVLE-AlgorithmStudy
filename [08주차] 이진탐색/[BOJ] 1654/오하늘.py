# 랜선 자르기
import sys
input = sys.stdin.readline

n,m = map(int, input().split()) # 가지고 있는 랜선의 개수, 필요한 랜선 개수
l = []
sum = 0

for i in range(n):
    a =  int(input())
    l.append(a)
    sum += a

def jogun(n):
    cnt = 0
    for i in range(n):
        if not l[i]/n > 0:
            return False
        else :
            cnt += l[i]//n
            if i == n-1:
                if cnt == m:
                    print(n)
                    return True
                else:
                    return False
            

limit = int(sum/m)
target = 0

# 0~limit
while 1:
    if jogun(limit):
        break
    else:
        limit = limit//2
        continue
