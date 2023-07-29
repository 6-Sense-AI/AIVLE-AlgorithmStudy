## 농장 뒷뜰에 일렬로 1번부터 N번까지 심었다
## 물뿌리개 2개 (1 또는 2), 함께 사용해서 3도 가능

n = int(input())
heights = list(map(int, input().split()))

## 물뿌리개 2개 뿌리면 전체 관점에서 3씩 자라남
## 총합이 3의 배수여야 함

total_height = sum(heights)

cnt = 0  ## 2짜리 물뿌리개 사용 횟수

if total_height % 3 == 0:
    for i in heights:
        cnt += i // 2

## 2짜리 물뿌리개 사용 횟수 = 1짜리 물뿌리개 사용 횟수
## 2짜리 물뿌리개 사용이 전체 키우는 기간보다 커야 함 (아니면 2짜리보다 1짜리를 많이 쓰게 되어서 전제 오류)
  
    if cnt >= (total_height / 3):
        print("YES")
    else:
        print("NO")
else:
    print("NO")


