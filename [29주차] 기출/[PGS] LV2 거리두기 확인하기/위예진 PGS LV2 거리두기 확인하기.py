# 테스트 3, 8, 31 틀림... 해결중

from itertools import permutations

# 응시자가 거리두기를 지키고 있는지 확인하는 함수
def is_human_safe(c_status, r, c):
    
    for moves in permutations([(-1, 0), (1, 0), (0, -1), (0, 1)], 2):
        mr, mc = r, c
        for dr, dc in moves:
            mr, mc = mr + dr, mc + dc
            
            if 0 <= mr < 5 and 0 <= mc < 5:    # 범위 확인
                # 자기 자신으로 돌아오면, 종료
                if (mr, mc) == (r, c): break
                
                if c_status[mr][mc] == 'X':    # 칸막이
                    break
                elif c_status[mr][mc] == 'P':    # 사람
                    return False
    
    return True

# 대기실이 거리두기를 지키고 있는지 확인하는 함수
def is_class_safe(c_status):
    for r in range(5):
        for c in range(5):
            if c_status[r][c] == 'P':
                if not is_human_safe(c_status, r, c):
                    return False
    
    return True
    
def solution(places):
    ans = []
    
    for c_status in places:
        if is_class_safe(c_status):
            ans.append(1)
        else:
            ans.append(0)
    
    return ans