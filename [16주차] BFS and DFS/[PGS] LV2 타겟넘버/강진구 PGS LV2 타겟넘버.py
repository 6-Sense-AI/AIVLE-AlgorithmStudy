def dfs(num, start, target):
    ans = 0
    if not num and start == target:
        return 1
    elif not num and start != target:
        return 0
    else:
        ans += dfs(num[1:], start+num[0], target)
        ans += dfs(num[1:], start-num[0], target)
        
        return ans
    

def solution(numbers, target):
    answer = dfs(numbers, 0, target)
        
    return answer