# 퇴사 2
# 예제 4 빼고 통과 _ 수정 중
import sys
input = sys.stdin.readline

day = int(input()) #날짜
info = []
for i in range(day):
    info.append(list(map(int, input().split()))) # 정보

dp = [0] * day
result = [0]*day

for i in range(day): # 수익구하기
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