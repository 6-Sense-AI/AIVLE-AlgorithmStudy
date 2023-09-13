

##  G킬로그램은 성원이의 현재 몸무게의 제곱에서 성원이가 기억하고 있던 몸무게의 제곱을 뺀 것

g = int(input())

left = 1
right = 1
result = []

while True:
    diff = right**2 - left**2

    
    if right - left == 1 and diff > g: 
        break    

    if diff > g: 
        left += 1
    elif diff < g: 
        right +=1
    else:
        result.append(right)
        right += 1

if result: 
    print(*result, sep='\n')
else: 
    print(-1)