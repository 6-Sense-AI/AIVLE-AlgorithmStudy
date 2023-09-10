import sys

input = sys.stdin.readline

n, m = map(int, input().split())

seq = list(map(int, input().split()))

i, j = 0, 0
cnt = 0

while j<=n:
    seq_sum = sum(seq[i:j])

    if seq_sum > m:
        i += 1
    else:
        if seq_sum == m:
            cnt += 1
        j += 1
        
print(cnt)