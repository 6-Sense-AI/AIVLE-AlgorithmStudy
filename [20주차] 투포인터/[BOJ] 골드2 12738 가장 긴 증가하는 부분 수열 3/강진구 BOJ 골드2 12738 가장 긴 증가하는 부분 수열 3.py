import sys

input = sys.stdin.readline

n = int(input())
seq = list(map(int, input().split()))

def binary_search(start,end,target):
    if start > end:
        return start
       
    mid = (start+end) // 2
    
    if res[mid] > target:
        return binary_search(start,mid-1,target)
    elif res[mid] == target:
        return mid
    else:
        return binary_search(mid+1,end,target)

res = [seq[0]]
# res 라는 배열에 증가하는 수열을 저장할 건데 처음부터 끝까지 돌려서 큰게 있다면 집어넣고 아니라면 해당 값을 인덱스로 찾아서 앞에 res 인덱스에 넣어줌
for i in range(1,n):
    if res[-1] < seq[i]:
        res.append(seq[i])
    else:
        res[binary_search(0,len(res)-1,seq[i])] = seq[i]


print(len(res))