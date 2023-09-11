import sys
input = sys.stdin.readline

# n: 일 수, target: 인출 횟수
n, target = map(int, input().split())
# 매일 이용할 금액 리스트
days = list(int(input()) for _ in range(n))
# 최대 인출 금액(전체 일수에서 필요한 금액 총합)으로 초기화
ans = sum(days)    

# 매일 필요한 금액보다는 인출 금액이 커야하므로
# 최소 금액을 가장 큰 금액으로 설정
left, right = max(days), ans
while left <= right:
    mid = (left + right) // 2
    # 현재 인출한 금액, 횟수(처음에 1회 인출하고 시작)
    now, cnt = mid, 1    

    # 전체 일수 돌면서 확인
    for mon in days:

        if now < mon:    # 갖고 있는 금액 적으면, 더 인출
            cnt += 1
            now = (mid - mon)
        else:    # 충분히 크면, 현재에서 빼주기
            now -= mon

    # 인출 횟수가 목표보다 클 때, 인출값 키워주기
    if cnt > target:
        left = mid + 1
    else:
        ans = min(ans, mid)    # 현재값, 이전값 비교해서 작은 것 넣어주기
        right = mid - 1

print(ans)