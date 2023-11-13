from collections import deque

def solution(rows, cols, queries):
    ans = []
    rotated = [[False] * (cols + 1) for _ in range(rows + 1)]
    moves = [(0, 1), (1, 0), (0, -1), (-1, 0)]    # 시계방향
    
    for r1, c1, r2, c2 in queries:
        nr, nc = r1, c1
        m = 0
        
        if not rotated[nr][nc]:
            rotated[nr][nc] = (nr - 1) * cols + nc
        nxt = deque([rotated[nr][nc]])
        tmp = rotated[nr][nc]
        
        while True:
            dr, dc = moves[m]
            mr, mc = nr + dr, nc + dc
            
            if r1 <= mr <= r2 and c1 <= mc <= c2:    # 범위 내 확인
                nr, nc = mr, mc    # 이동
                
                if not rotated[nr][nc]:    # 이동한 적 없다면,
                    nxt.append((nr - 1) * cols + nc)
                    rotated[nr][nc] = nxt.popleft()
                else:    # 이동한 적 있다면,
                    nxt.append(rotated[nr][nc])
                    rotated[nr][nc] = nxt.popleft()
                    
                tmp = min(tmp, nxt[0])
            else:
                m = (m + 1) % 4
                continue
            
            if (nr, nc) == (r1, c1):
                break
        
        ans.append(tmp)
        
    return ans