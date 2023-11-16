num = 1000 - int(input())
pay = [500, 100, 50, 10, 5, 1]
cnt = 0

for i in pay:
    cnt += num // i
    num %= i
    
print(cnt)
