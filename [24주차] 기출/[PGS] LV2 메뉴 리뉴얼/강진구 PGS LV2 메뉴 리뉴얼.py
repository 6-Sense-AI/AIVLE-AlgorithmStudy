from itertools import combinations as cb
from collections import Counter
def solution(orders, course):
    answer = []
    maximum = 0
    for i in course:
        check = []
        for ord in orders:
            for c in cb(sorted(ord),i):  #sort(ord)
                check.append(c)
            cnt = Counter(check)
        for m in cnt.most_common(1):
            maximum = m[1]
        for c in cnt.most_common():
            if c[1] == maximum and maximum >= 2:
                answer.append(c[0])
    ans_lst = []
    for ans in answer:
        word = ''
        for a in ans:
            word+=a
        ans_lst.append(word)
    return sorted(ans_lst)