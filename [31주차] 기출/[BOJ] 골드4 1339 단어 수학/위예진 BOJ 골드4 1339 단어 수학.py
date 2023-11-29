# 해결

from collections import defaultdict
import sys
input = sys.stdin.readline

n = int(input())
words = []
weights = defaultdict(int)    # 각 알파벳의 가중치 저장
alp_to_num = dict()    # 각 알파벳에 대응하는 숫자 사전

# 단어 저장하며, 알파벳 가중치 저장
for _ in range(n):
    w = list(input().rstrip())
    words.append(w)
    for i in range(len(w)):
        weights[w[i]] += 10 ** (len(w) - i)

# 가중치순으로 알파벳 역순 정렬
weights = sorted(weights.items(), key=lambda x: -x[1])

# 알파벳 대응 사전 채우기
ni = 9
for alp, _ in weights:
    alp_to_num[alp] = ni
    ni -= 1

# 숫자 연산
ans = 0
for w in words:
    w_num = ''
    for alp in w:
        w_num += str(alp_to_num[alp])

    ans += int(w_num)

print(ans)