
targets = [[0,1],[1,4],[2,3],[3,4]]

answer = 0
# 답 : 최소 요격 미사일
# 예제도 맞고 반례도 다 돌려봤는데 맞음
# 하지만 테케서 틀림 왜인진 모르겠음
targets.sort(key=lambda x: x[1])
print(targets)

check = -1
for i in range(len(targets)):
    if check <= targets[i][0]: # 진입 기준
        check = targets[i][1]
        answer += 1
print(answer)