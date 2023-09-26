import sys
input = sys.stdin.readline

num_plates, kinds, window, coupon = map(int, input().split())
plates = list(int(input()) for _ in range(num_plates))

eats = [0] * (kinds + 1)    # 먹은 접시 표시 리스트
eats[coupon] = 1    # 쿠폰 넣어주기
cnt = 1    # 현재 초밥 가짓수
for i in plates[:window]:
    if not eats[i]:    # 먹은 적 없다면, 가짓수 늘려주기
        cnt += 1
    eats[i] += 1    # 먹은 개수 갱신
max_cnt = cnt    # 초밥 최대 가짓수 초기화

# 한 바퀴 돌면서 탐색
for i in range(num_plates):
    # 다음 접시 넣어주기
    end = plates[(i + window) % num_plates]
    if not eats[end]:    # 먹은 적 없다면, 가짓수 늘려주기
        cnt += 1
    eats[end] += 1

    # 이전 접시 빼주기
    srt = plates[i]
    eats[srt] -= 1
    if not eats[srt]:    # 먹은 접시 리스트에 없다면, 가짓수 빼주기
        cnt -= 1

    # 초밥 최대 가짓수 갱신
    max_cnt = max(max_cnt, cnt)

print(max_cnt)