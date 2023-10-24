
num, length = map(int,input().split())
time = 0
cur_loc = 0 ## 현재 위치 저장

for _ in range(num):
    loc, red, green = map(int,input().split())

    time += loc-cur_loc ## 첫 신호등 위치까지 이동

    cur_loc = loc

    if time%(red+green) <=red:
        time += (red-time%(red+green))

time+=(length-cur_loc) ## 마지막 신호등 끝나고 도로 끝까지 이동

print(time)







