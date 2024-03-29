def solution(rows, columns, queries):
    # 행렬 생성
    matrix = [[row * columns + col + 1 for col in range(columns)] for row in range(rows)]
    answer = []
    
    for t, l, b, r in queries:
        top, left, bottom, right = t-1, l-1, b-1, r-1
        tmp = matrix[top][left]
        minimum = tmp # 가장 작은 수

        #위
        for y in range(top, bottom):
            value = matrix[y+1][left]
            matrix[y][left] = value
            minimum = min(minimum, value)

        #왼 
        for x in range(left, right):
            value = matrix[bottom][x+1]
            matrix[bottom][x] = value
            minimum = min(minimum, value)

        #아래    
        for y in range(bottom, top, -1):
            value = matrix[y-1][right]
            matrix[y][right] = value
            minimum = min(minimum, value)
        #오    
        for x in range(right, left, -1):
            value = matrix[top][x-1]
            matrix[top][x] = value
            minimum = min(minimum, value)
        
        #겹치는부분 처리
        matrix[top][left+1] = tmp
        answer.append(minimum)
        
    return answer

rows = 6
columns = 6
queries = [[2,2,5,4],[3,3,6,6],[5,1,6,3]]

print(solution(rows, columns, queries))