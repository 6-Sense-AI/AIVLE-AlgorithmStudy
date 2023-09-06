n, m, r = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
do = list(map(int, input().split()))


def one(n, m):
    for i in range(m):
        for j in range(n // 2):
            arr[j][i], arr[(n - 1) - j][i] = arr[(n - 1) - j][i], arr[j][i]
