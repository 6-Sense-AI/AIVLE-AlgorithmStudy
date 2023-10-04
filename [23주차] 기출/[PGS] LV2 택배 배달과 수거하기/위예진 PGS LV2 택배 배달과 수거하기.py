def solution(cap, n, deliveries, pickups):
    ans = 0    # 최단 이동거리
    deli = 0    # 배달해야 할 택배 수
    pick = 0    # 가져와야 할 택배 수
    
    # 가장 거리가 먼 곳부터 순회
    for i in range(n-1, -1, -1):
        # i번째 집의 배달, 픽업 택배 수 더해줌
        deli += deliveries[i]
        pick += pickups[i]
        
        # 하나라도 양수이면, 한 번에 모두 처리 불가능 -> 거리 더해줘야 함
        # 모두 음수이면, 한 번에 모두 처리 가능 -> 거리 더해줄 필요 X
        while deli > 0 or pick > 0:
            deli -= cap
            pick -= cap
            ans += (i + 1) * 2
            
    return ans