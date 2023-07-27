import sys

s = input()
rvs_s = s[::-1]

rvs_s_lst = list(rvs_s.split())
rvs_s_lst.reverse()

for i in rvs_s_lst:
    print(i, end=' ')
