import sys
input =sys.stdin.readline

# 입력받기
n = int(input())
num = list(map(int, input().split()))
result = [0] * n


for i in range(n):
    cnt = 0
    for j in range(n):
        if cnt == num[i] and result[j] == 0:
            result[j] = i + 1
            break
        elif result[j] == 0:    # 앞이 0인 경우 
            cnt += 1

print(' '.join(map(str,result)))