n = int(input())
people = list(map(int, input().split()))
ans = [False] * n

ans[people[0]] = 1
for now in range(1, n):

    res = people[now]    # 본인보다 키가 큰 사람의 수

    for i in range(n):
        if ans[i]:    # 배정된 위치이면, 다음 위치로 넘어가기
            continue

        if res == 0:    # 자신보다 키가 큰 사람이 더이상 없을 때, 배치
            ans[i] = now + 1
            break

        res -= 1

print(*ans)