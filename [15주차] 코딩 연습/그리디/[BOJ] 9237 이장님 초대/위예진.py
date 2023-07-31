# 입력 받기
n = int(input())    # 묘목의 수
t = list(map(int, input().split()))    # 각 나무가 자라는 데 걸리는 시간(일)

# 가장 오래 걸리는 나무부터 심기
t.sort(reverse=True)     # 내림차순 정렬

# 나무가 심기는 날짜를 더해줌 (1일부터 시작)
for i in range(n):
    t[i] += (i + 2)    # 심는 날도 포함해줘야 하므로

print(max(t))    # 가장 오래 걸리는 날 출력