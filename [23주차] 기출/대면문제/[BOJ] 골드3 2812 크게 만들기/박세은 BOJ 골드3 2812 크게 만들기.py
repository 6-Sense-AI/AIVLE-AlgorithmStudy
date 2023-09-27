## 런타임 에러 남 ㅠㅠ ##
## 예제 다 맞음 ##

n, k = map(int, input().split())
num = input()
num_list = list(map(int, str(num)))

start = num_list.index(max(num_list[0:k]))

k -= start

ans = [num_list[start]]
i = start + 1

while k != 0:
    if ans[-1] < num_list[i]:
        ans.pop()
        ans.append(num_list[i])
        k -= 1

        if i < len(num_list):
            i += 1
        else:
            break
        
    else:
        ans.append(num_list[i])

        if i < len(num_list):
            i += 1
        else:
            break

for j in range(i, n):
    ans.append(num_list[j])

print("".join(map(str, ans)))
