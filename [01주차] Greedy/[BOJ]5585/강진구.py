import sys
ans = 0

price = int(sys.stdin.readline())
money = 1000-price

m_lst = [500,100,50,10,5,1]

for i in range(6):
    x =  money//m_lst[i]
    ans += x
    money -= m_lst[i]*x

print(ans)
