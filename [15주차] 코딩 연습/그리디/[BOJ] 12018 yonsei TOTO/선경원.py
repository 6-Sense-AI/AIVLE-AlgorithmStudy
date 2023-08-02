n, m = map(int,input().split()) ## 과목 수, 마일리지

answer = 0 ## 신청 과목 수




class_mil = [] ## 수업에 사용하는 마일리지


for i in range(n):
    p, l = map(int, input().split())
    milage_ppl = list(map(int, input().split())) 
    milage_ppl.sort(reverse=True).
  
    ## P가 L보다 작거나 같은 경우 마일리지 1만 써도 먹을 수 있다

    if p <= l:
        class_mil.append(1)

   ## 아닌 경우 가장 적게 써서 수강인원 안에만 들면 된다
    else:
        mile = milage_ppl[l - 1]
        class_mil.append(mile)

class_mil.sort()
for class_m in class_mil:
    if m - class_m >= 0:
        answer += 1
        m -= class_m
print(answer)
