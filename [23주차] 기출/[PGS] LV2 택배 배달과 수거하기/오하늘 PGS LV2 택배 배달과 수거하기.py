def solution(cap, n, deliveries, pickups):
    # 제출했는데 이상하게 올라와 있어서 다시 제출함
    # 최대개수, 집, 택배 상자, 빈 재활용 상자
    t = [0, 0]
    answer = 0 # 최소 이동거리

    for idx in range(n-1, -1, -1): # 거꾸로 해야함

        t[0] += deliveries[idx]
        t[1] += pickups[idx]

        while t[0] > 0 or t[1] > 0:
            t[0] -= cap
            t[1] -= cap
            answer += (idx + 1) * 2
    return answer