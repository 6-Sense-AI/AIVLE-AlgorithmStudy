# 큰사각형에서 작은 사각형을 꺾인 지점 기준으로 만들어 주려고 했는데 시작점에 따라 잡아주는게 복잡해서 답을 확인했습니다.
# 가장 긴변을 기준으로 양 옆을 빼주면 무조건 빠지는 부분이 나오게 됩니다.

import sys

input = sys.stdin.readline

n = int(input())

sqr = [list(map(int, input().split())) for _ in range(6)]

max_w, w_idx = 0,0
max_h, h_idx = 0,0

for i in range(6):
    if sqr[i][0] == 1 or sqr[i][0] == 2:
        if max_w<sqr[i][1]:
            max_w = sqr[i][1]
            w_idx = i
    else:
        if max_h<sqr[i][1]:
            max_h = sqr[i][1]
            h_idx = i

sub_w = abs(sqr[(w_idx-1)%6][1]-sqr[(w_idx+1)%6][1])
sub_h = abs(sqr[(h_idx+1)%6][1]-sqr[(h_idx-1)%6][1])

print(n*((max_h*max_w)-(sub_w*sub_h)))