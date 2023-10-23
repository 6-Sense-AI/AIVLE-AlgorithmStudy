import math
def cal_money(fees,time):
    return fees[1] + math.ceil(max(0, (time - fees[0])) / fees[2]) * fees[3]

def solution(fees, records):
    answer = []
    info = {}
    st = {}
    
    for p in records:
        time, num, chk = p.split()
        hour, minute = map(int,time.split(":"))
        time = hour * 60 + minute

        if chk == 'IN' : # 입차
            info[num] = time
            
        elif chk == 'OUT' :
            try :
                st[num] += time - info[num]
            except :
                st[num] = time - info[num]
            del info[num]
            
    for num, minute in info.items():
        try:
            st[num] += 23*60+59 - minute
        except:
            st[num] = 23*60+59 - minute      
            
    print(st)
    print(info)
    
    return [cal_money(fees, time) for num, time in sorted(list(st.items()), key=lambda x: x[0])]
    
            
            
    return answer
fees = 	[180, 5000, 10, 600]
records = ["05:34 5961 IN", "06:00 0000 IN", "06:34 0000 OUT", "07:59 5961 OUT", "07:59 0148 IN", "18:59 0000 IN", "19:09 0148 OUT", "22:59 5961 IN", "23:00 5961 OUT"]
print(solution(fees, records))