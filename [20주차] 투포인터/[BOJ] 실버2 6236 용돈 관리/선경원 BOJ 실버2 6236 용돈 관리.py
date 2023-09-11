

n, m = map(int,input().split())  ## 사용일 수, 인출 횟수
spend = []

for i in range(n):
    cost = int(input())
    spend.append(cost)

## 인출 금액 K가 max(spend) 보다 크거나 같아야 함
## 매일 필요한 금액의 총합보다 많이 인출할 필요 없음

left = max(spend)
right = sum(spend) 

while left <= right:
    mid = (left + right) // 2
    money = mid  ## 인출 금액

    ## 처음에 무조건 인출
    cnt = 1

    ## 1일 비용이 인출액보다 크면 인출
    ## 아니면 인출액을 각 날짜의 거스름돈으로 업데이트
    for i in spend:
        if money - i < 0:
            money = mid
            cnt += 1
        money -= i

    ## m보다 많이 인출했거나 최대 금액보다 적게 인출했을 경우 
    ## left를 올려서 인출액을 올린다

    if cnt > m or mid < max(spend):
        left = mid + 1
    else:
        right = mid - 1
        ans = mid

print(ans)


