import sys
input = sys.stdin.readline

n = int(input())
tmp = list(input().rstrip())
signal = []
# 1, 0 값을 갖도록 변경
for i in range(5):
    signal.append(tmp[i * (n // 5):(i + 1) * (n // 5)])

# 숫자들
numbers = [
    '####.##.##.####',    # 0
    '#' * 5,    # 1
    '###..#####..###',    # 2
    '###..####..####',    # 3
    '#.##.####..#..#',    # 4
    '####..###..####',    # 5
    '####..####.####',    # 6
    '###..#..#..#..#',    # 7
    '####.#####.####',    # 8
    '####.####..####',    # 9
]

now = 0
while now < n // 5:

    # 숫자 시작 확인
    if signal[0][now] == '#':

        # 하나의 숫자만 뽑기
        single_num = ''.join(sum([s[now:now + 3] for s in signal], []))
        
        if single_num in numbers:    # 1 제외 나머지
            print(numbers.index(single_num), end='')
            now += 4
        else:    # 1
            print(1, end='')
            now += 2
    else:
        now += 1