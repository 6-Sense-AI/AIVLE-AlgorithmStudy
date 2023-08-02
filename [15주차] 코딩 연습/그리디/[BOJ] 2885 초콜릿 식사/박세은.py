k = int(input()) # 상근이가 필요한 정사각형 개수
s = 1 # 초콜릿 최소 크기
c = 0 # 쪼개기 카운트

while s < k: 
    s *= 2

sc = s 

if s == k: 
    print(s, c)

else: 
    while k != 0: 
        if sc // 2 <= k:
            c += 1
            k -= sc // 2
            sc = sc // 2
            
        
        else:
            c += 1
            sc = sc // 2
    
    print(s, c)
