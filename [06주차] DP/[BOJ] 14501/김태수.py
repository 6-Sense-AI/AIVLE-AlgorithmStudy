n = int(input())
dic = {}
num =[]


for i in range(n):
    a, b = map(int, input().split())
    dic[a] = {b}
