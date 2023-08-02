n = int(input())

tree = list(map(int, input().split()))


if sum(tree)%3 != 0:
    print('NO')
else:
    if sum(tree)%2 >= sum(tree)%3:
        print('YES')
    else:
        print('NO')
