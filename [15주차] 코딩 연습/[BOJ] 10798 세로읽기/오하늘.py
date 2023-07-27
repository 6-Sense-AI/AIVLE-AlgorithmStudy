import sys
input = sys.stdin.readline

arr = []
max = 0
for _ in range(5):
    temp = list(input().strip())
    arr.append(temp)
    if len(temp) > max : max = len(temp)
ans = ''
print(max)

for i in range(0,max):
    for j in range(0,5):
        if arr[j][i] == '\n' or arr[j][i] == None:
            continue
        else : ans += str(arr[j][i])
print(ans)
