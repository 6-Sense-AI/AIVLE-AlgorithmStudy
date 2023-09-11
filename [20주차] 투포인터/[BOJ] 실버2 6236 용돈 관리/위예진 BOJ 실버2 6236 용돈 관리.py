import sys
input = sys.stdin.readline

# n: 일 수, target: 인출 횟수
n, target = map(int, input().split())
# 매일 이용할 금액 리스트
days = list(int(input()) for _ in range(n))
ans = sum(days)    # 최대 인출 금액으로 초기화

left, right = min(days), ans
while left <= right:
    mid = (left + right) // 2

    now, cnt = mid, 1    # 현재 인출한 금액, 횟수
    for mon in days:

        if now < mon:    # 갖고 있는 금액 적으면, 더 인출
            cnt += 1
            now = (mid - mon)
        else:    # 충분히 크면, 현재에서 빼주기
            now -= mon

    if cnt > target or mid < max(days):
        left = mid + 1
    else:
        ans = min(ans, mid)
        right = mid - 1

print(ans)