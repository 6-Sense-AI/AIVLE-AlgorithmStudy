import sys
input = sys.stdin.readline

# n: 수열의 길이, target: 만들고자 하는 합
n, target = map(int, input().split())
nlist = list(map(int, input().split()))    # 수열
ans = 0    # 경우의 수

left, right = 0, 0
while left <= right and right <= n:
    now = sum(nlist[left:right])    # 현재 합
    
    if now == target:
        ans += 1
        right += 1
    elif now < target:
        right += 1
    else:
        left += 1

print(ans)

########################### 의문점 해결 ###########################
# 현재 합 부분을 아래와 같이 설정하면, 아래 테스트 케이스 충족 X
# now = sum(nlist[left:right+1])    # 현재 합

# (반례)
# 입력
# 4 1
# 1 2 3 1

# 출력
# 1

# 답
# 2

# 이유는, left와 right가 만나고, 
# 총합이 0이 되어 다시 시작하는 부분이 필요하기 때문!
# 따라서 [left:right+1] 와 같이 무조건 값 하나를 선택하게 되면 정답에 도달할 수 X