# # 예제는 다 맞는다 -> 메모리 초과
# # 근데 내가 봐도 상당히 비효율적
# import sys
# input = sys.stdin.readline
# from itertools import combinations

# n, k = map(int, input().split())
# num = int(input())

# num_str = str(num)
# split = []
# for i in num_str:
#     split.append(int(i))

# long = len(num_str)
# number = list(range(0, long))
# a = list(combinations(number, k))

# a_len = len(a)
# a_lenlen = len(a[0])
# result = []

# for i in range(a_len):
#     tmp = list(split)

#     for j in range(a_lenlen):
#         bb = a[i][j]
#         tmp[bb] = 11
#     while 11 in tmp:
#         tmp.remove(11)
#     sum = 0
#     for digit in tmp:
#         sum = sum * 10 + digit
#     result.append(sum)

# result.sort(reverse=True)
# print(result[0])

N, K = map(int, input().split())
num = list(input())
k = K
stack = []

for i in range(N):
    while(k > 0 and stack and stack[-1] < num[i]):
        stack.pop()
        k-=1
    stack.append(num[i])
    
print(''.join(stack[:N-K]))