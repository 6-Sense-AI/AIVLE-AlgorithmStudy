# 넘 어려워서 풀이 봄!
# PyPy3로 해야 시초 안남,,,,!

# n번 세로선이 n번에 도착하는지 확인하는 함수
def reach_nn():
    for ver in range(v):
        srt = ver
        for hor in range(h):
            if ladder[hor][srt]:    # 오른쪽에 연결선 존재
                srt += 1    # 사다리 이동
            elif srt > 0 and ladder[hor][srt-1]:    # 왼쪽에 연결선 존재
                srt -= 1    # 사다리 이동

        if srt != ver:    # n-n 도착 아닐 시
            return False
        
    return True

# 가로선 놓는 함수
def set_connect(cnt, x, y):
    global ans

    # 종료 확인
    if cnt >= ans:    # 현재 최소값보다 크거나 같을 경우
        return
    if reach_nn():    # 연결이 잘 됐는지
        ans = min(ans, cnt)
        return
    elif cnt == 3:    # 문제조건 넘어갈 경우
        return
    
    # 가로선 놓기
    for i in range(x, h):

        # 가로선을 우선으로 탐색하므로
        if i == x:    # 행이 변경되기 전에는 가로선을 계속해서 탐색
            k = y 
        else:    # 행이 변경될 경우, 가로선 처음부터 탐색
            k = 0 

        for j in range(k, v - 1):    # 세로선(열)
            # 연속적으로 연결하면 안되므로,
            # 가로선을 놨을 때 양쪽에 연결선이 존재하지 않는 경우
            if not ladder[i][j] and not ladder[i][j + 1]:   # 오른쪽 고려
                if j > 0 and ladder[i][j - 1]:     # 왼쪽 고려
                    continue 
                ladder[i][j] = True    # 가로선 놓기

                # cnt 1 증가, 세로선 그대로, 
                # 위아래 연속(=)이 되면 안되므로 가로선은 2증가
                set_connect(cnt + 1, i, j + 2) 
                ladder[i][j] = False    # 가로선 다시 없애주기

if __name__ == '__main__':
    v, c, h = map(int, input().split())    # 세로선, 놓은 연결선, 가로선의 수
    ladder = [[False] * v for _ in range(h)]     # 특정 지점 방문 여부 체크

    # c가 0이면, 종료
    if c == 0: 
        print(0)
        exit(0)

    # 연결선 정보 입력 받기
    for _ in range(c):
        nh, nv = map(int, input().split())
        ladder[nh-1][nv-1] = True    # 연결

    ans = 4    # 결과값 4로 초기화
    set_connect(0, 0, 0)

    print(ans if ans < 4 else -1)
    