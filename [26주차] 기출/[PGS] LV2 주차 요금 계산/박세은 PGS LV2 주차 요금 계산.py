# 풀다가 뇌정지와서 멈춤

import math

idx = [['0000', 1, 'IN', [6, 0]], ['0000', 2, 'OUT', [6, 34]], ['0000', 5, 'IN', [18, 59]], ['0148', 4, 'IN', [7, 59]], ['0148', 6, 'OUT', [19, 9]], ['5961', 0, 'IN', [5, 34]], ['5961', 3, 'OUT', [7, 59]], ['5961', 7, 'IN', [22, 59]], ['5961', 8, 'OUT', [23, 0]]]
fees = [180, 5000, 10, 600]

ans = []

i = 1

def timer(cnt, time):
    global i

    while True:
        if idx[i][0] == idx[i-1][0] and idx[i][2] != idx[i-1][2]:
            print('im 1')
            time += (idx[i][3][0] * 60 + idx[i][3][1]) - (idx[i-1][3][0] * 60 + idx[i-1][3][1])

            if idx[i][0] != idx[i-1][0] and idx[i][2] != idx[i-1][2]:
                 i += 1
                 break
            
            else:
                 i += 2

        elif idx[i][0] != idx[i-1][0] and idx[i][2] == idx[i-1][2]:
            print('im 2')
            time += (23 * 60 + 59) - (idx[i-1][3][0] * 60 + idx[i-1][3][1])
            i += 1
            break
    
    print('Im here')
    if time <= fees[0]:
        cnt = fees[1]
                        
    else:
        cnt = fees[1] + (math.ceil(time) / fees[2]) * fees[3]
    
    return cnt

if len(idx) > 1:
    while i < len(idx):
        ans.append(timer(0, 0))
                
                            
else:
    time = (23 * 60 + 59) - (idx[0][3][0] * 60 + idx[0][3][1])
    if time <= fees[0]:
        cnt = fees[1]
        print(cnt)
                        
    else:
        cnt = fees[1] + (math.ceil(time) / fees[2]) * fees[3]
        print(cnt)
            

print(ans)