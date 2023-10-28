
height, width = map(int,input().split()) 

blocks = list(map(int, input().split()))   
rain = 0  


## 양 끝에 블록은 신경쓰지 않아도 됨

## 주변 둘러싼 블럭 중 낮은 거 높이만큼 물이 고임

## 가로에서 각 칸마다 확인해서 고이는 물의 양에 더해주자

for i in range(1, width - 1):
    max_left = max(blocks[:i])
    max_right = max(blocks[i+1:])

    min_height = min(max_left, max_right)
    if blocks[i] < min_height:
        rain += (min_height - blocks[i])

print(rain)