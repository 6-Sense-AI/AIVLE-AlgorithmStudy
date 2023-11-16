X = 64
x = int(input())
list = []
count = 1

while X != 0 :
    list.append(X)
    X = X // 2

if x in list :
    print(count)

else:
    for i in list:
        if x > i :
            x = x - i
            count += 1
    print(count)
