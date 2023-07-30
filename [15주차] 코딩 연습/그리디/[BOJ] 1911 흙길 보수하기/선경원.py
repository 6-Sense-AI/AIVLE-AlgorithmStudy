N, L = map(int, input().split())  ## 웅덩이 개수, 널빤지 길이 입력

answer = 0  ## 널빤지 개수

## 널빤지 위치 입력
pod_loc = []
for i in range(N):
  start, end = map(int,input().split())
  pod_loc.append((start, end))

pod_loc.sort()  ## 웅덩이 위치 정렬


point = pod_loc[0][0] ## 이어붙인 널빤지 표시
cnt = 0
for start, end in pod_loc:
    if point > end:  ## 한 웅덩이에서 널빤지 붙인 게 end 이상이면 패스 (웅덩이 아닌 부분)
        continue
    elif point < start:  ## 널빤지 붙인 게 start보다 이전이면 start로 갱신
        point = start
    dist = end - point  ## 널빤지 깔린 곳부터 웅덩이 End 지점까지 간격

  
    r = 1  ## 웅덩이 간격이 L보다 크면 널빤지 하나는 더 붙는다
    if dist % L == 0:
        r = 0  ## 웅덩이 간격을 널빤지로 딱 맞게 채우기
    count = dist//L + r
    point += count*L ## 시작점에서 널빤지를 이어붙이고 마지막 끝자락
    cnt += count
print(cnt)
