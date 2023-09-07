# G킬로그램은 성원이의 현재 몸무게의 제곱에서 성원이가 기억하고 있던 몸무게의 제곱을 뺀 것

# g = now^2 - rem^2
g = int(input())     
ans = []    # 가능한 현재 몸무게
m = 100000    # g는 100,000보다 작거나 같은 자연수

srt, now = 1, 1    # 몸무게는 0보다 큰 수이므로, 1로 초기화
while srt <= m and now <= m:    # 최대로 가능한 수만큼 순회

    tmp = now ** 2 - srt ** 2

    if tmp == g:    # 같다면, 리스트에 추가
        ans.append(now)
    if tmp < g:    # 작은 동안에, 현재 몸무게 늘려주기
        now += 1
        continue
    srt += 1    # 크다면, 예상 몸무게 늘려주기

if ans:
    for i in ans:
        print(i)
else:
    print(-1)