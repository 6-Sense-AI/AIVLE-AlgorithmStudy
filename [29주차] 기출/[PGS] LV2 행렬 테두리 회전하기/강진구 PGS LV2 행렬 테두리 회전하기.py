from collections import deque
def solution(rows, columns, queries):
    answer = []
    mat = [[] for _ in range(rows)]
    for i in range(1,rows+1):
        for j in range(1,columns+1):
            mat[i-1].append((i-1)*columns+j)
    
    que = deque(queries)
    
    while que:
        x1,y1,x2,y2 = que.popleft()
        
        d1 = deque([])
        for j in range(y1-1,y2):
            d1.append(mat[x1-1][j])
        x = d1.pop()
        
        d2 = deque([])
        for i in range(x1,x2):
            d2.append(mat[i][y2-1])
        d2.appendleft(x)
        x = d2.pop()
        
        d3 = deque([])
        for j in range(y1-1,y2-1):
            d3.append(mat[x2-1][j])
        d3.append(x)
        x = d3.popleft()
        
        d4 = deque([])
        for i in range(x1,x2-1):
            d4.append(mat[i][y1-1])
        d4.append(x)
        x = d4.popleft()
        
        d1.appendleft(x)
        
        for j in range(y1-1,y2):
            mat[x1-1][j] = d1[j-y1+1]
        
        for i in range(x1,x2):
            mat[i][y2-1] = d2[i-x1]
        
        for j in range(y1-1,y2-1):
            mat[x2-1][j] = d3[j-y1+1]
        
        for i in range(x1,x2-1):
            mat[i][y1-1] = d4[i-x1]
        
        
        min_v = rows*columns
        if d1:
            min_v = min(min(d1),min_v)
        if d2:
            min_v = min(min(d2),min_v)
        if d3:
            min_v = min(min(d3),min_v)
        if d4:
            min_v = min(min(d4),min_v)
        answer.append(min_v)
    
    return answer