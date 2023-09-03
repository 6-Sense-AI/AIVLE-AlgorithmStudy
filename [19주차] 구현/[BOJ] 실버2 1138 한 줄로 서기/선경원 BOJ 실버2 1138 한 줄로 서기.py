

## 사람 수 입력

n = int(input())

## 왼쪽에 키 큰 사람 얼마나 있는지 입력

left_taller = list(map(int,input().split()))   ##  [2, 1, 1, 0]

answer = [0]*n 


## 숫자들 중 위치 확정이 가능한 1부터 시작

for i in range(n):   
    cnt = 0  ## 숫자 위치 찾기
    for j in range(n):
        
        if cnt == left_taller[i] and answer[j] == 0:
            answer[j] = i + 1
            break  ## 찾았으면 종료
        elif answer[j] == 0:
            cnt += 1
                
print(' '.join(map(str, answer)))


