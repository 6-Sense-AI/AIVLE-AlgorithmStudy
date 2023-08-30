# 퇴사 2
# 예제 4 빼고 통과 _ 수정 중
import sys
input = sys.stdin.readline

day = int(input()) #날짜
info = []
tmp = []
for i in range(day):
    info.append(list(map(int, input().split()))) # 정보
    if  i + info[i][0] > day : tmp.append(i)

dp = [0] * day
result = [0]*day


# 첫번째 방법 - 예제 4 틀림 가능한 모든 인덱스는 돌아봐야 함
for i in range(day): # 수익구하기
    if i + info[i][0] > day : break # 6과 7의 경우
    k = i
    temp = 0
    while 1 :
        if k >= day: break # 날짜를 넘으면
        if k+info[k][0] > day :
            k += 1
            if k >= day : break
            else : continue
        temp += info[k][1]
        dp[k] = max(info[k], temp)
        k = k+info[k][0]
    result[i] = temp

print(max(result))

# 두번쨰 방법 전략
# 가능한 인덱스는 모두 구해놓음
for i in range(day): # 수익구하기
    if i + info[i][0] > day : break # 6과 7의 경우
    
    for j in range(i,len(tmp)): # 가능한 모든 수를 구하고 최대 출력
        # 이거로 최대를 계속 갱신하는 점화식을 세울 것임.
        dp[i] = max(dp[i], info[i][1]+info[j]) # 이전 vs 다음꺼랑 비교
    
print(dp[day-1])