c, h, t = map(int, input().split())    # 원판, 숫자, 회전의 수
clocks = [[False] * h] + [list(map(int, input().split())) for _ in range(c)]    # 원판의 정보
turns = [list(map(int, input().split())) for _ in range(t)]    # 회전 정보


# 평균 계산해서 작은 수, 큰 수 처리
def cal_avg():
    total, cnt = 0, 0

    # 평균 계산
    for i in range(1, c+1):
        total += sum(clocks[i])
        cnt += (h - clocks[i].count(False))
    if cnt:
        avg = total / cnt
    else:    # 전부 False 이면, 무시
        return

    for i in range(1, c+1):
        for j in range(h):
            if not clocks[i][j]:     # 삭제된 칸 무시
                continue

            if clocks[i][j] < avg: clocks[i][j] += 1
            elif clocks[i][j] > avg: clocks[i][j] -= 1

# 회전 수행
for idx, dir, cnt in turns:

    # 번호가 idx의 배수인 원판을 dir방향으로 cnt칸 회전시킴
    for i in range(idx, c + 1, idx):
        if dir == 0:    # 시계 방향
            clocks[i] = clocks[i][-cnt:] + clocks[i][:-cnt]
        else:    # 반시계 방향
            clocks[i] = clocks[i][cnt:] + clocks[i][:cnt]

    # 인접하면서 같은 수 찾아 처리
    s_list = set()
    for i in range(1, c+1):
        for j in range(h):

            if not clocks[i][j]:    # 제거된 부분 넘기기
                continue

            # 인접하면서 같은 수이면, 리스트에 넣어줌
            for mi, mj in [(i-1, j), (i+1, j), (i, j-1), (i, (h+j+1) % h)]:
                if 0 < mi <= c and clocks[i][j] == clocks[mi][mj]:
                    s_list.add((mi, mj))

    # 인접한 수가 있다면, 수들을 바꾸기
    if s_list:
        for i, j in s_list:
            clocks[i][j] = False
    # 없다면, 평균 계산
    else:
        cal_avg()

print(sum(sum(clocks, [])))