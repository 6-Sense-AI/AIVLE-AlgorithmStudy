def solution(n, m, x, y, r, c, k):
    # 최대한 위로 안올라가게 하고 왔다갔다 할때는 좌우로
    # d, l, r, u(사전 순)
    
    answer = ''
    if abs(r-x)+abs(c-y) > k:
        answer = 'impossible'
    elif (k-(abs(r-x)+abs(c-y)))%2 == 1:
        answer = 'impossible'
    else:
        while k>0:
            if r>x:
                answer+='d'
                x+=1
            elif c<y:
                answer+='l'
                y-=1
            elif c>y:
                answer+='r'
                y+=1
            else:
                if x-r<k:
                    if c > 1:
                        answer+='l'
                        y-=1
                    elif c == 1:
                        answer+='r'
                        y+=1
                else:
                    answer+='u'
                    x-=1
                        
            k-=1
            if x==r and y==c and k%2==1:
                answer = 'impossible'
                break
    return answer

# 생각한 방법은 아래로 왼쪽으로가 우선이고 좌우가 도달했을 때 만약 위로 가야하는데 k가 여유가 있으면 좌우로 왔다갔다 하고
# k가 위로 올라갈 만큼만 남으면 그만큼 u를 추가하는 형태를 만들려고 했는데 어떤거에서 안된걸까요