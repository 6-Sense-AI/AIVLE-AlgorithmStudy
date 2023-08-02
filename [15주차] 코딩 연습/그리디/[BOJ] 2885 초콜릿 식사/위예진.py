# 정사각형(2^n)을 계속 반으로 쪼갰을 때, 남은 것들을 더해서 k를 만들어야 함
# k보다 큰 최소 정사각형부터 시작!
import math

k = int(input())    # 상근이가 먹어야 할 최소 정사각형 모양의 초콜릿 수

choco = 2 ** math.ceil(math.log2(k))    # 가장 작은 초콜릿의 크기
n = 0    # 쪼개는 횟수
now = 0    # 현재까지 더한 초콜릿 수
splt = choco    # 쪼개고 남은 초콜릿 수

while now < k:    # 상근이가 초콜릿을 모두 먹으면, 종료
    
    if (k - now) >= splt:    # 필요한 초콜릿 크기가 쪼갠 초콜릿보다 크다면, 모두 먹기
        now += splt
    else:    # 그렇지 않다면, 초콜릿 쪼개기
        n += 1    # 쪼개는 횟수 늘리기
        splt //= 2    # 초콜릿 쪼개기

print(choco, n)