import sys
input = sys.stdin.readline


n = int(input())

arr = [0]*n # 초기 배열
info = list(map(int, input().split())) # 정보

# 0의 갯수를 제외하고 순서대로 채워주면 된다.
for i in range(n):
    cnt = 0
    for j in range(n):
        if cnt == info[i] and arr[j] == 0:
            arr[j] = i + 1 # 값 넣어줌
            break
        elif arr[j] == 0 : cnt += 1 # 0일때만 cnt 올려줌

print(' '.join(map(str,arr)))