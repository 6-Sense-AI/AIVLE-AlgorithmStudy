import sys
input = sys.stdin.readline
# 참외밭
# 1,2와 3,4로 구분
# 큰 사각형 - 작은 사각형 (변의 길이의 차가 작은 사각형)
n = int(input())

w = [] # 폭
h = [] # 높이
t = [] # 전체

for _ in range(6):
    d, tmp = map(int, input().split())
    if d ==1 or d==2: #동쪽 서쪽
        w.append(tmp)
        t.append(tmp)
    else : # 남 북
        h.append(tmp)
        t.append(tmp)

w_max = t.index(max(w)) # 최대 폭
h_max = t.index(max(h)) # 최대 높이

# 구현은 참고했다.. 작은 사각형 구하는 법을..
s1 = abs(t[w_max-1] - t[(w_max-5 if w_max ==5 else w_max+1)])
#5인경우 최대폭이 오른쪽에 위치하므로 빼야할 변은 맨왼쪽변이기에 -5 이외에는 바로 이전의 변을 구해야하므로 +1
s2 = abs(t[h_max-1] - t[(h_max-5 if h_max ==5 else h_max+1)])

ans = (max(w) * max(h) - s1*s2) * n
print(ans)