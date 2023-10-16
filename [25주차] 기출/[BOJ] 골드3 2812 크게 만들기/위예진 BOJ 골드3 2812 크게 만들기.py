# combinations 썼더니 역시나 시초남,,,
# 해설 보고 그리디로 풀었음

# n: 숫자의 자릿수, k: 지울 숫자의 수
n, k = map(int, input().split())
number = list(input())    # 해당 숫자
rest = k    # 남은 지울 횟수
s = []    # 남길 숫자들을 저장할 스택

# 숫자의 처음부터 끝까지 한번씩 확인
for i in range(n):
    # 지울 횟수가 남아있고, 스택에 숫자가 있다면,
    # 현재 숫자보다 작은 수들을 스택에서 지움
    while rest > 0 and s and s[-1] < number[i]:
        s.pop()
        rest -= 1    # 지울 횟수 줄여주기
    
    # 현재 숫자를 스택에 추가함
    s.append(number[i])

print(''.join(s[:n-k]))