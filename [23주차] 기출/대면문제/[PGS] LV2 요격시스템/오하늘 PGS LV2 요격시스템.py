
targets = [[0,1],[1,4],[2,3],[3,4]]

answer = 0
# 답 : 최소 요격 미사일
# 예제도 맞고 반례도 다 돌려봤는데 맞음
# 하지만 테케서 틀림 왜인진 모르겠음
targets.sort()
print(targets)

i = 1
while 1:
    if i >= len(targets) : break
    temp = targets[i-1][1] # 이전값의 끝값
    tt = targets[i][1]
    while i < len(targets):

        if targets[i][1] < tt:
            tt = targets[i][1]
        if temp > targets[i][0] : # 작으면 계속 돌아
            if i >= len(targets) : break
            # 이때! 또다른 n의 끝값이 다음길이 첫번째보다 작으면 answer+=1 해야함
            if tt <= targets[i][0]: answer+=1
            i += 1
            continue
        else :
            i+=1
            answer +=1
            break

print(answer+1)