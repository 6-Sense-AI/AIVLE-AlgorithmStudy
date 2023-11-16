

## 입력받기

import sys
k, n = map(int, sys.stdin.readline().split()) ## 가지고 있는 개수, 만들고 싶은 개수
lines = []
for _ in range(k):
    line = int(sys.stdin.readline())
    lines.append(line)
lines.sort() 



## 0부터 가장 짧은 랜선 길이 사이의 숫자로 하면 
## left = 0, right = min_line-1로 설정 이지 탐색

left = 1
right = max(lines)


while left<=right:
    count = 0  ## 만들게 되는 랜선 개수 카운트
    mid = (left + right)//2
    for i in lines:
        count +=i //mid
        
    if count >=n:  ## n 이상이면 left 옮겨오기
        left = mid +1
    else:   ## 아니면 right 옮기기
        right = mid - 1
        
print(right)
