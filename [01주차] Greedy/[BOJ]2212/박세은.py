n = int(input()) 
k = int(input())
x = list(map(int, input().split()))
x2 = []
result = []
min = 0

for v in x :
    if v not in x2 :
        x2.append(v)

x2.sort(reverse = True)
      
for i in x2 : 
    for j in x2 :
        sub = i - j
        result.append(sub)
print(result)

for t in result :
    if t < 0 :
        result.remove(t)
        
result.sort(reverse = True)


for h in range(k-1, 0, -1) :
    min += result[h]  
    
print(min)