n = int(input())  # 계단 개수
scr = [int(input()) for _ in range(n)]  # 계단 점수
ans = [0] * n  # 최댓값 기록

if n < 3:  # 계단이 3개 이하면 총 합 리턴
    print(sum(scr))

else:
    # 두번째 계단까지의 최댓값 기록
    ans[0] = scr[0]
    ans[1] = scr[0] + scr[1]

    for i in range(2, n):  # 3번째 계단부터 최댓값 검사
        ans[i] = max(
            ans[i - 3] + scr[i - 1] + scr[i], ans[i - 2] + scr[i]
        )  # (두 계단 연속 오름, 건너뛰고 오름) 중에 더 큰 값 리턴

    print(ans[-1])  # 도착지 최댓값 출력
