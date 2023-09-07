# 백곰이 위치한 부분도 잊으면 안된다!!!! 전체 길이는 (step + 1 + step)
import sys
input = sys.stdin.readline

# n: 양동이의 수, step: 닿을 수 있는 거리
n, step = map(int, input().split())
ice = [0] * 10000001
end = 0
for _ in range(n):
    g, x = map(int, input().split())
    ice[x] = g
    end = max(end, x)

moves = sum(ice[:step * 2 + 1])    # 이동하며 더하게 되는 얼음들의 합
ans =  moves   # 얼음들의 합의 최대값

for gom in range(step, end - step + 1):
    moves += (- ice[gom - step] + ice[gom + step + 1])     # 현재 위치의 얼음들의 합
    ans = max(ans, moves)    # 최대값 갱신

print(ans)