from itertools import combinations_with_replacement

# 응시자가 거리두기를 지키고 있는지 확인하는 함수
def is_human_safe(c_status, r, c):
    
    # 맨해튼 거리로 확인하므로, 이동 가능 방향에서 중복으로 2개를 뽑아서 만들어야 함
    for moves in combinations_with_replacement([(-1, 0), (1, 0), (0, -1), (0, 1)], 2):
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