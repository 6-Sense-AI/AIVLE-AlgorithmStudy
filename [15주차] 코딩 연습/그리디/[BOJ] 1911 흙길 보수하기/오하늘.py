# 흙길 보수하기 실1
import sys
input = sys.stdin.readline

N, L = map(int, input().split()) # 물 웅덩이 개수, 널빤지 길이
arr = []
for i in range(N):
    arr.append(list(map(int, input().split())))
arr.sort() # 정렬

cnt = 0
for i in range(N):
    tmp = arr[i][1] - arr[i][0]
    while True:
        if tmp <= 0 :
            t = -tmp
            if i+1 <= N-1:
                if arr[i+1][0] < arr[i][1]+t:
                    arr[i+1][0] = arr[i][1]+t # 끝 값 갱신
            break
        tmp -= L
        cnt+=1
print(cnt)

# 1차 시도 : 시간 초과
