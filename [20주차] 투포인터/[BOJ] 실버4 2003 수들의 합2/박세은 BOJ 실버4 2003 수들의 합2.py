n, m = map(int, input().split())
arr = list(map(int, input().split()))

cnt = 0 # 정답 카운트
asum = 0 # 배열의 현재 합

end = 0 # 현재 배열의 끝점

# 만약 asum이 m 보다 작다면 end를 뒤로 옮겨가며 더해줌,
# m 보다 크거나 같으면 start를 앞으로 옮겨주며 빼준다.
# start와 end가 끝에 도달할 때 까지 반복

for start in range(n): # while문 하나만 쓰면, start가 끝에 도달하기 전에 끝날 위험이 있으므로 2중 반복문 사용
    while asum < m and end < n : # asum의 크기와 end가 리스트 범위를 넘지 않는지 확인
        asum += arr[end]
        end += 1
    
    if asum == m:
        cnt += 1
    
    asum -= arr[start] # 반복문과 if문 모두 해당되지 않는다면 asum >= m 라는 뜻 이므로 arr[start]만큼 빼준다

print(cnt)

