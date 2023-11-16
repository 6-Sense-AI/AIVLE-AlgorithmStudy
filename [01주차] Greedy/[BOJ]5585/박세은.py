pay = int(input()) # 입력값
change = 1000 - pay # 거스름돈
coin = [500, 100, 50, 10, 5, 1] # 동전
count = 0 # 동전 개수

for i in coin :
    count += change // i
    change = change % i
    
print(count)
