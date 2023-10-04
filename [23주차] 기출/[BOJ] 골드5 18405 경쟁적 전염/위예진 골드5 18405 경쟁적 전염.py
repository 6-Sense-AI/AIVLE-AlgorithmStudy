import sys
input = sys.stdin.readline

n, k = map(int, input().split())    # 시험관 개수, 바이러스 종류의 수
virus = []    # 바이러스 정보
box = []    # 시험관
for i in range(n):
    box.append(list(map(int, input().split())))
    for j in range(n):
        if box[i][j] > 0:
            virus.append((box[i][j], i, j))
virus.sort()    # 바이러스 숫자가 작은 순서대로 정렬
sec, x, y = map(int, input().split())    # sec초 뒤, (x, y) 위치

move = [(-1, 0), (1, 0), (0, -1), (0, 1)]
# 바이러스 전염 함수
def spread_virus(virus):

    new_virus = []
    for v, x, y in virus:
        for mx, my in move:    # 상하좌우 전파
            tx, ty = x + mx, y + my
            if 0 <= tx < n and 0 <= ty < n:
                if not box[tx][ty]:
                    box[tx][ty] = v
                    new_virus.append((v, tx, ty))
    
    return new_virus

for s in range(sec):
    virus = spread_virus(virus)

print(box[x-1][y-1])