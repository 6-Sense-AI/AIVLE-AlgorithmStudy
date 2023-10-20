import math

def solution(fees, records):
    mon = dict()
    cars = dict()
    
    # 주차 시간 계산해서 저장
    for r in records:
        time, cid, check = r.split()
        h, m = map(int, time.split(':'))
        
        if check == 'OUT':
            tmp = (h * 60 + m) - cars[cid]

            if cid in mon:
                mon[cid] += tmp
            else:
                mon[cid] = tmp
                
            del cars[cid]
        else:
            cars[cid] = h * 60 + m
    
    # IN 정보만 있는 차량 처리
    for c in cars:
        tmp = (23 * 60) + 59 - cars[c]
        if c in mon:
            mon[c] += tmp
        else:
            mon[c] = tmp
            
    # 주차 요금 계산
    for a in mon:
        q = mon[a] // fees[0]
        money = fees[1]
        if q > 0:
            r = mon[a] - fees[0]
            money += math.ceil(r / fees[2]) * fees[3]

        mon[a] = money
    
    # 차량 번호순으로 정렬
    ans = []
    for d in sorted(mon):
        ans.append(mon[d])
    
    return ans 