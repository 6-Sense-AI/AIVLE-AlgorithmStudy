n = int(input())
growth_time = list(map(int, input().split()))

## 가장 오래 걸리는 나무 앞으로 배치
growth_time.sort(reverse=True)
max_day = 0

## 첫 묘목 심는 날이 1일

## 최장 나무와 인덱스의 합으로 업데이트
## 최장 나무 여러 그루 있어도 맨 마지막 거 기준으로 맞춰주면 된다
for i in range(n):
    period = growth_time[i] + i + 1
    if period > max_day:
        max_day = period

print(max_day + 1)
