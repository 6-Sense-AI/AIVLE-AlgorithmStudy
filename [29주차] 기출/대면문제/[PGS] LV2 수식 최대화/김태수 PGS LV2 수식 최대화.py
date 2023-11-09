# 그냥 함수를 따로 만들까?...
# stack을 이용해야하나?...
import re
from itertools import permutations

def calculation(a, b, item):
    if item = '+':
        return str(int(a) + int(b))
    elif item = '-':
        return str(int(a) - int(b))
    elif item = '*':
        return str(int(a) + int(b))      

def solution(expression):
    patters = r'(\d+|[+\-*/])'
    tokens = re.findall(patters,expression)
    tokens_l = len(tokens)
    cal = ['+', '-', '*']
    answer = []
    tmp1 = []
    tmp2 = []
    tmp3 = []
    for item in permutations(cal,3):
        for i in range(len(tokens_l)):
            tmp = tokens
            if tmp[i] == item:
                num = calculation(tmp[i-1], tmp[i+1], item)
                del.tmp(i-1)
                del.tmp(i)
                del.tmp(i+1)
                tmp.insert(i-1, num)
        tmp1.append(tmp)
    return tmp