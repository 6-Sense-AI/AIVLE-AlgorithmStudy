# 현재 범위 밖에서 선언된 변수를 '읽기'는 가능하지만, '변경'은 불가능하다!
# 따라서, 아래와 같이 선언을 해줘야 함!!
# global: 전역변수로 선언
# nonlocal: 전역변수 X, 현재 범위의 지역변수도 아닐 때 선언
# 참고 (https://juhi.tistory.com/6)

def solution(numbers, target):
    ans = 0
    
    # +/-로 가지가 계속 뻗어나감, 어차피 모든 경우의 수 확인해야 함
    # -> bfs/dfs 둘 다 상관 없을 듯
    # now_idx: 현재 트리 깊이, now_sum: 현재까지의 합
    def make_target(now_idx, now_sum):
        nonlocal ans    # 전역 변수가 아닌데, 현재 함수 내의 지역변수도 아닐 때는 nonlocal로 선언!
        
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