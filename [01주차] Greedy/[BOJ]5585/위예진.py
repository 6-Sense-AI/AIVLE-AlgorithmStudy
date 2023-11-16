change = 1000 - int(input())    # n: 거스름돈
money = [500, 100, 50, 10, 5, 1]    # 잔돈의 종류
res = 0    # 결과(잔돈의 개수)

for m in money:
    if change >= m:
        res += change // m    # 해당 잔돈의 개수
        change = change % m    # 잔돈을 뺀 나머지 금액

print(res)
