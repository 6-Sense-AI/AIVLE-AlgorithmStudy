# 최대 상자에서 작은 부분을 뺀다
# 작은 상자 부분 못구해서 정답확인
import sys
input=sys.stdin.readline

s = [] 
x = [] # 가로 길이
y = [] # 세로 길이
lownum = [] # 작은상자

k = int(input())

for i in range(6):
    way,dist = map(int,input().split()) # 방향, 거리 입력
    s.append([way,dist])
    if s[i][0] == 3 or s[i][0] == 4: # 세로 저장
        x.append(s[i][1])
    if s[i][0] == 1 or s[i][0] == 2: # 가로 저장
        y.append(s[i][1])

# 작은상자 길이 추출
for i in range(6):
    if s[i][0] == s[(i+2)%6][0]:
        lownum.append(s[(i+1)%6][1])
        
print( ((max(x)*max(y)) - (lownum[0]*lownum[1])) * k )