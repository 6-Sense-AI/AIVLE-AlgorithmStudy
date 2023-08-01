# 이장님 초대
import sys
input = sys.stdin.readline

n = int(input()) # 묘목
max = 0

arr = list(map(int,input().split()))
arr.sort(reverse=True) # 내림차순 정렬

for i in range(n):
    tmp = i+1+arr[i] # index+걸리는 시간
    if tmp > max : max = tmp

print(max+1) # 묘목 심기
