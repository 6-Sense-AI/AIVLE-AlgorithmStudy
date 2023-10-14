from collections import deque

def solution(n, m, x, y, r, c, k):

    # 이동 경로 사전순으로 정렬
    moves = [(1, 0, 'd'), (0, -1, 'l'), (0, 1, 'r'), (-1, 0, 'u')]
    q = deque([(x, y, '')])
    
    while q:
        x, y, route = q.popleft()
        cnt = len(route)    # 이동횟수
            
        # 목표에 도달했을 때,
        if (x, y) == (r, c):
            # 목표횟수만큼 이동했다면, 성공
            if cnt == k:
                return route
            # 홀수개만 추가로 더 이동할 수 있다면, 실패
            if (k - cnt) % 2 == 1:
                return 'impossible'

        # 모든 방향으로 이동시키기
        for ir, ic, d in moves:
            mr = x + ir
            mc = y + ic
            
            # 미로 범위를 넘어가지 않고, 이동 횟수를 넘어가지 않으면, 
            # 사전 순으로 더 빠른 경로로 탈출해야 하므로 큐에 추가하고, 종료
            if 0 < mr <= n and 0 < mc <= m:
                if abs(mr - r) + abs(mc - c) + cnt + 1 <= k:
                    q.append((mr, mc, route + d))
                    break
    
    return 'impossible'