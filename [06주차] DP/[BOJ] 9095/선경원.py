## 주어진 정수를 1 2 3의 합으로 나타내는 방법

## 정수는 11보다 작다

# 1은 0개, 2는 1개, 3은 2개, 4는 7개, 5는 

# 0 1 2 4  7 13 24 44 ... 274(10)


T= int(input())
mem = [0]*(T+1)
for i in range(T):
    num = int(input())

    
def plus(n):    

    if n == 0:
        return 0
    elif n == 1:
        return 1
    elif n == 2:
        return 2
    elif mem[n]!=0:
        return mem[n]
    
    mem[n] = mem[n-3] + mem[n-2] + mem[n-1]
    return mem[n]


print(plus(num))
