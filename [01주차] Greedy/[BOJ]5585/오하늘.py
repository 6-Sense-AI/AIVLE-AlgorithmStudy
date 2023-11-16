# for문이랑 효율성으로 크게 차이 없어서 그냥 while문 이용햇어요

money = 1000-int(input())
cnt = 0
while True :
    if money == 0:
        break
    if money>=500:
        money-=500
        cnt += 1
        continue
    if money>=100:
        money-=100
        cnt += 1
        continue
    if money>=50:
        money-=50
        cnt += 1
        continue
    if money>=10:
        money-=10
        cnt += 1
        continue
    if money>=5:
        money-=5
        cnt += 1
        continue
    if money>=1:
        money-=1
        cnt += 1
        continue
print(cnt)

