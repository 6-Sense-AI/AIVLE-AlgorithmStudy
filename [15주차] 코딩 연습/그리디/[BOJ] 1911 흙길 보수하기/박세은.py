import sys
input = sys.stdin.readline

n, l = map(int, input().split()) # 웅덩이 개수, 널빤지 길이
lst = [] # 웅덩이 위치 리스트

for _ in range(n):
    n1, n2 = map(int, input().split())
    lst.append(n1)
    lst.append(n2)

lst.sort()

ans = 0 # 정답

for i in range(0, len(lst) - 1, 2):
    c = 0 # 웅덩이 크기
    u = 0 # 사용해야하는 널빤지 갯수
    o = 0 # 널빤지 잉여 길이

    c = lst[i+1] - lst[i]

    if c % l != 0: # 나머지가 있으면 널빤지 갯수+1
        u = (c // l) + 1
        o = (u*l) - c
        ans += u

    else :
        u = c // l
        o = (u*l) - c
        ans += u

    if  i + 2 < len(lst): # 만약 다음 웅덩이와 현재 웅덩이 사이 거리가 잉여 길이보다 짧다면, 잉여 길이만큼 웅덩이 크기 줄여주기
        if lst[i+2] - lst[i+1] < o:
            lst[i+2] = lst[i+2] + o - (lst[i+2] - lst[i+1])

    

print(ans)
