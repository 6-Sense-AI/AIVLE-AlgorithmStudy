import sys
input = sys.stdin.readline

n, k = map(int, input().split()) # 얼음 양동이 갯수, 움직일 수 있는 거리

st = 10000001
end = 0

# 첫번째 시도 왜 틀렸을까.. 일단은 시간초과이므로 문제가 있다!
d = [0] * 10000001
end = 0
for _ in range(n):
    i, j = map(int, input().split()) # 얼음 양, 좌표
    d[j] = i
    if j < st : st = j
    if j > end : end = j

result = 0
for i in range(st+k-1,end-k):
    cnt = 0
    for j in range(i-k, i+k+1):
        if d[j] != 0 : cnt += d[j]
    if cnt > result : result = cnt

print(result)