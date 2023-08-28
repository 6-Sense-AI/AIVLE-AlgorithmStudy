

## 계단은 한 번에 한 계단씩 또는 두 계단씩

## 3연속 불가

## 마지막 계단은 무조건 밟음

## 즉 첫 계단은 1번 아니면 2번

n = int(input())

score = [int(input()) for _ in range(n)]


## 점프 한 번 뛰고 나면 거기서부터 다시 시작

dp=[0]*(n)

## n = 1이면 score를 반환

if len(score)<=2:
    print(sum(score))

## 3회 내로 최대한 사용해야 한다
## 2칸 점프인지 1칸 점프인지 비교해서 최대값으로 반환

else:
    dp[0] = score[0]
    dp[1] = score[0]+score[1]
    for i in range(2,n):
        dp[i]=max(dp[i-3]+score[i-1]+score[i], dp[i-2]+score[i])
        
    print(dp[-1])


