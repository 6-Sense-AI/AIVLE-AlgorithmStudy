import sys
input = sys.stdin.readline

# 입력받기
k = int(input())

# 초콜릿 크기 및 쪼개는 횟수 
num = 1
cnt = 0

# 초콜릿 최소크기 구하기
while num < k:
    num = num * 2
result1 = num

# 쪼개는 횟수 구하기
while True:
    if k % num == 0:
        result2 = cnt
        break
    else:
        num = num // 2
        cnt = cnt + 1
print(result1, result2)
