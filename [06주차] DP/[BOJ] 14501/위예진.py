import sys
input = sys.stdin.readline

n = int(input())    # 퇴사 전 일하는 일수
term = [0]    # 걸리는 시간(id 0은 0으로 초기화)
pay = [0]    # 급여
total = [0] * (n + 1)
for _ in range(n):
    t, p = map(int, input().split())
    term.append(t)
    pay.append(p)
    
for d in range(1, n + 1):
    cnt = total[d]    # 지금까지의 최대 급여로 초기화
    now = d    # 현재 위치
    while now <= n:
        tmp = now + term[now]
        
        if tmp <= n:
            total[now] = max(cnt + pay[now], total[now])
            now += term[now]
        else:
            now += 1

print(total)
print(max(total))