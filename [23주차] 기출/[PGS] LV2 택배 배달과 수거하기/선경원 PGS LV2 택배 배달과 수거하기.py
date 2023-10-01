def solution(cap, n, deliveries, pickups):
        
    ## deliveries : 배달 
    ## pickups : 수거
    
    ## 뒤에 있는 집부터 배달 / 수거해 오는 게 최소한의 거리

    
    deliveries = deliveries[::-1]
    pickups = pickups[::-1]
    answer = 0

    deli = 0
    pick = 0

    for i in range(n):
        deli += deliveries[i]
        pick += pickups[i]

        while deli > 0 or pick > 0:
            deli -= cap
            pick -= cap
            answer += (n - i) * 2  ## 왕복거리 2배

    return answer     
    