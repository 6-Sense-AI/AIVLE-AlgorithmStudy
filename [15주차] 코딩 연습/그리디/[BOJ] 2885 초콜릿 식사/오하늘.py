# 초콜릿 식사
import sys
input = sys.stdin.readline

# 조건 1 : 초콜릿의 크기는 항상 2의 제곱형태
k = int(input()) # 필요한 초콜렛의 크기

size = 2 # 구매해야 하는 초콜렛의 크기
while True :
    if k <= size : break
    size *= 2
ans = size

# 조건 2 : 초콜릿을 자르지 않아도 됨 ( 4+2 형태여도 합이 6이기만 하면 됨 )
cnt = 0
temp = 0
while True:
    if temp == k or ans == k: break # input과 맞춰짐, input == k의 경우
    size /= 2
    if temp + size > k : # 초코 사이즈가 k보다 큰 경우
        cnt += 1
        continue
    else :
        temp += size
        cnt += 1

print(ans, cnt)
