n = int(input())
std = [] # 학생 정보
grp=[] * (n**2) # 자리표

for _ in range(n**2):
    std.append(list(map(int, input().split())))

for i in range(n**2):
    
