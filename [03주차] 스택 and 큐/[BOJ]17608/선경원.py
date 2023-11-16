import sys

n=int(sys.stdin.readline())
stick = [int(sys.stdin.readline().rstrip()) for _ in range(n)]
count=0

# i번째 기둥이 그 뒤 기둥들 최대값보다 커야보인다.
    
for i in range(len(stick)):
    max_stick = max(stick[i+1:])
    if stick[i] > max_stick:
        count +=1                  
print(count+1)
        
        
