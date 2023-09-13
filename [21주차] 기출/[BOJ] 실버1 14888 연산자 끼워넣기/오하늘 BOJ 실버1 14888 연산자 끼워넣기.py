import sys
input = sys.stdin.readline

arr_n = int(input()) # 수 갯수
arr = list(map(int,input().split()))
cal_info = list(map(int,input().split()))
# 덧셈, 뺄셈, 곱셈, 나눗셈
cal = []
for i in range(4):
    if cal_info[i] != 0 :
        for _ in range(cal_info[i]):
            if i == 0 : cal.append('P') # 더하기
            if i == 1 : cal.append('M') # 빼기
            if i == 2 : cal.append('X') # 곱하게
            if i == 3 : cal.append('N') # 나누기
# 수식
def solution(arr, cal):
    temp = arr[0]
    for i in range(len(cal)):
        if cal[i] == 'P': temp += arr[i+1]
        if cal[i] == 'M': temp -= arr[i+1]
        if cal[i] == 'X': temp *= arr[i+1]
        if cal[i] == 'N':
            if temp > 0 : #양수
                temp //= arr[i+1]
            else : # 음수
                temp *= -1
                temp //= arr[i+1]
                temp *= -1
    return temp


# 순열
from itertools import permutations # 순열 라이브러리

max_ans = -1e9 # 최대
min_ans = 1e9 # 최소
for i in permutations(cal,len(cal)):
    mid_ans = solution(arr, i)
    if mid_ans > max_ans : max_ans = mid_ans
    if mid_ans < min_ans : min_ans = mid_ans

print(max_ans)
print(min_ans)