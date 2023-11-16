

num=1000-int(input())

coin=[500,100,50,10,5,1]
count=0
for i in coin:
    count+=num//i
    num%=i
print(count)



## 이렇게 푸는게 그리디가 맞는지 모르겠지만 일단 풀어봤씁니다

## 입력받는 값은 num으로 하고, 각 동전을 coin이라는 리스트에 담았습니다.

## 금액이 큰 동전부터 사용해, count에는 거스름돈을 동전으로 나눈 몫을,

## num에는 거스름돈을 동전으로 나눈 나머지를 배정했습니다.
