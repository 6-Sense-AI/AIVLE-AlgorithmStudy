import sys
input = sys.stdin.readline

n, m = map(int,input().split()) # 수의 갯수, 되야하는 수
arr = list(map(int,input().split()))
cnt = 0
rt = 1 # 오른쪽
lt = 0 # 왼쪽

# 이분탐색은 start = 0 end = n 에서 양쪽에서 좁혀간다면
# 투포인터는 둘다 0 이고 계속 바뀌어주는 알고리즘이다. 이분탐색으로 생각했다가 시간 오래걸림 ㅜ

while lt<=rt:
    if rt > n : break
    temp = sum(arr[lt:rt])
    if temp == m :
        cnt+=1
        rt += 1
    elif temp > m :
        lt += 1
    else :
        rt += 1
print(cnt)