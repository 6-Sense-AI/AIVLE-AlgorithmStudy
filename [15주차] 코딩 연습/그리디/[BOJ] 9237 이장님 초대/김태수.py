import sys
input = sys.stdin.readline

# 입력
n = int(input())
t = list(map(int, input().split()))
# 내림차순 정렬
t.sort(reverse=True)

# 묘목 자라는 날짜 계산을 위한 result 생성
result = []
for i in range(n):
    result.append(t[i] + i + 1)

print(max(result) + 1)
