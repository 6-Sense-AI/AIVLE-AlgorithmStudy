# n: 신호등의 개수, l: 도로의 길이
n, l = map(int, input().split())    
now, t = 0, 0     # 현재 위치, 걸린 시간
for _ in range(n):
    # d: 신호등의 위치, r, g: 빨간색, 초록색이 지속되는 시간
    d, r, g = map(int, input().split())

    # 이동 시간 추가
    t += (d - now)    
    now = d

    # 기다리는 시간 추가
    cycle = r + g
    tmp = t % cycle
    if 0 <= tmp < r:
        t += (r - tmp)

# 마지막 신호등 이후에 걸린 시간 계산
t += (l - now)

print(t)