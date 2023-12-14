# 풀이 봄
# 43%에서 계속 틀림
# -> 해결: 최대값(1e9) 또는 최소값(-1e9)일 때, 소수점까지 포함되어 출력되어, int형으로 바꿔줌

import sys
input = sys.stdin.readline

n = int(input())    # 수의 개수
nums = list(map(int, input().split()))    # 숫자 리스트
ops = list(map(int, input().split()))    # 연산자들의 수 (덧셈, 뺄셈, 곱셈, 나눗셈)

res_min = int(1e9)
res_max = int(-1e9)

# 백트래킹
def dfs(cnt, now):
    global res_min, res_max

    # 종료 조건
    if cnt == n:
        res_min = min(res_min, now)
        res_max = max(res_max, now)
        return
    
    # 하나씩 확인하기
    if ops[0] > 0:    # +
        ops[0] -= 1
        dfs(cnt + 1, now + nums[cnt])
        ops[0] += 1
    if ops[1] > 0:    # -
        ops[1] -= 1
        dfs(cnt + 1, now - nums[cnt])
        ops[1] += 1
    if ops[2] > 0:    # *
        ops[2] -= 1
        dfs(cnt + 1, now * nums[cnt])
        ops[2] += 1
    if ops[3] > 0:    # /
        ops[3] -= 1
        dfs(cnt + 1, int(now / nums[cnt]))
        ops[3] += 1

dfs(1, nums[0])

print(res_max)
print(res_min)