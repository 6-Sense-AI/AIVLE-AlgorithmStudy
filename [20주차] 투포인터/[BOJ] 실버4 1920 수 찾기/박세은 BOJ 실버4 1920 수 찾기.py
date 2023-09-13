n = int(input())
lst = list(map(int, input().split()))

m = int(input())
exp = list(map(int, input().split()))

ans = [0 for _ in range(m)]

# 이진탐색을 위해 리스트를 정렬해준다
lst.sort()

# 이진탐색 (exp 위치, 시작점, 끝점, 중위수)
def search(i, start, end, mid):
    while start <= end :
        mid = (start + end) // 2 # 중위수 업데이트

        if lst[mid] == exp[i]: # 만약 중위수와 찾으려는 수가 같으면
            ans[i] = 1 # 1로 바꿔주고 반복문 탈출
            break
        
        elif lst[mid] > exp[i]: # 중위수가 찾으려는 수 보다 크다면
            end = mid - 1 # 중위수의 오른쪽에 있는 모든 수는 고려할 필요 없으므로 끝점을 중위수 앞번호로 바꿔준다
        
        elif lst[mid] < exp[i]: # 중위수가 찾으려는 수 보다 작다면
            start = mid + 1 # 중위수의 왼쪽에 있는 모든 수는 고려할 필요 없으므로 시작점을 중위수 앞번호로 바꿔준다

start = 0
end = n-1
mid = 0

for i in range(m):
    search(i, start, end, mid)
    print(ans[i])




