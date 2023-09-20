import sys
input = sys.stdin.readline
from itertools import combinations, permutations

n = int(input())
num = n//2
arr =[]
result = []     # 각각 더한 값들의 모임
final =[]       # 마지막 최소값들의 모임
for _ in range(n):
    arr.append(list(map(int, input().split())))

# 1. 만약 n=6이라면 0~5까지의 수가 담겨있는 long이라는 리스트를생성한다.
# 2. 한 팀은 n//2(num)만큼의 사람이 포함되어 있으므로 조합을 사용하여
#    모든 경우의 수를 a라는 리스트에 저장한다.
long = len(arr)
number = list(range(0, long))
a = list(combinations(number, num))

# 1. a의 행마다 능력치를 더하기 위해 각 행의 값들을 순열을 이용하여 
#    더한값을 sum에 저장후 result에 append한다.
for i in range(len(a)):
    sum = 0
    b = list(permutations(a[i], 2))
    for j in range(len(b)):
        x = b[j][0]
        y = b[j][1]
        sum = sum + arr[x][y]
    result.append(sum)

# 1. 차이의 최소값을 구하기 위해 인덱스를 이용하여 비교한다.
# 2. 비교값을 final에 저장
tmp = len(result)-1
mid = len(result)//2
for i in range(mid):
    if result[i] >= result[tmp-i]:
        final.append(result[i] - result[tmp-i])
    else:
        final.append(result[tmp-i] - result[i])

# final 리스트를 오름차순으로 정렬
final.sort()
# 가장 작은값 출력
print(final[0])