def solution(numbers, target):
    ans = 0
    
    # +/-로 가지가 계속 뻗어나감, 어차피 모든 경우의 수 확인해야 함
    # -> bfs/dfs 둘 다 상관 없을 듯
    # now_idx: 현재 트리 깊이, now_sum: 현재까지의 합
    def make_target(now_idx, now_sum):
        nonlocal ans
        
        # 숫자의 끝에 도달했으면, 종료
        if now_idx == len(numbers):
            if now_sum == target:    # 타겟 숫자를 만들었으면, 정답 추가
                ans += 1
            return 0
        
        # 모든 경우의 수(+, -) 탐색
        for oper in (numbers[now_idx], - numbers[now_idx]):
            make_target(now_idx + 1, now_sum + oper)
    
    make_target(0, 0)
    
    return ans