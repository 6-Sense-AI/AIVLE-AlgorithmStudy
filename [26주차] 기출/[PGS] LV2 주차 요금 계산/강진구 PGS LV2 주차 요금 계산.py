from collections import defaultdict, deque
import math
def time_cal(t1,t2):
    time = 0
    h1, m1 = t1.split(':')
    h2, m2 = t2.split(':')
    h1,m1,h2,m2 = int(h1),int(m1),int(h2),int(m2)
    if h2>=h1:
        if m2>=m1:
            time += (h2-h1)*60 + (m2-m1)
        else:
            time += (h2-h1-1)*60 +(m2+60-m1)
    else:
        if m1>=m2:
            time += (h1-h2)*60 + (m1-m2)
        else:
            time += (h1-h2-1)*60 +(m1+60-m2)
    return time

def solution(fees, records):
    answer = []
    dic = defaultdict(list)
    for record in records:
        t, n, io = record.split()
        dic[n].append((t,io))
    key = sorted(dic.keys())
    for k in key:
        que = deque([])
        que.extend(dic[k])
        time = 0
        t1 = ''
        while que:
            t, io = que.popleft()
            if io == 'IN':
                t1 = t
            else:
                time += time_cal(t1,t)
            
            if len(que) == 0  and io == 'IN':
                time += time_cal(t1,'23:59')
        if time<=fees[0]:
            answer.append(fees[1])
        else:
            answer.append(fees[1]+(math.ceil((time-fees[0])/fees[2]))*fees[3])
        
        
    return answer