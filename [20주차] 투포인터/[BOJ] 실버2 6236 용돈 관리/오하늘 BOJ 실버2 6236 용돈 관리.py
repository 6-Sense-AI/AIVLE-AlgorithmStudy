import sys
input = sys.stdin.readline

n, m = map(int,input().split()) # 남은 일 수, 돈 빼는 횟수

arr = []
for i in range(n):
    arr.append(int(input()))

# 정답
min = min(arr)
max_v = sum(arr) # 이것도 처음에 max()로 줬다가 틀림..ㅜ0ㅜ

result = 0

while min <= max_v :
    mid = (min+max_v)//2 # 중간값
    
    cnt = 1
    t = mid
    for i in arr:
        if t < i:
            cnt += 1
            t = mid
        t -= i

    if cnt > m or mid < max(arr):
        min = mid+1
    else :
        result = mid
        max_v = mid - 1

print(result)


# 처음에 썼던 방법 예제는 되는데 시간초과 why?

tmp = list(set(arr))
tmp.sort() # 최소부터 최대
min = tmp[0] #최소
max = tmp[-1] #최대

result = 0
t = len(tmp)//2
mid = tmp[t]
while min <= max : # 이분탐색 조건
    charge = mid

    cnt = 1
    for i in range(len(arr)):
        if charge < arr[i]:
            cnt += 1
            charge = mid
        charge -= arr[i]

    if cnt > m or mid < max:
        t += 1
        if t > 0 and t<m :
            max = tmp[t]
            mid = tmp[t]
        else : break
    elif cnt == m:
        result = tmp[t]
        break
        
    else:
        result = tmp[t]
        t -= 1
        if t > 0 and t<m :
            min = tmp[t]
            mid = tmp[t]
        else : break

print(result)