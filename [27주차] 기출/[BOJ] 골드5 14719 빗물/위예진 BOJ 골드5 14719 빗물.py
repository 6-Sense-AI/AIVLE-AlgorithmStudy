row, col = map(int, input().split())    # 블록의 최대 가로, 세로
blocks = list(map(int, input().split()))    # 블록의 높이들
rains = 0    # 고이는 빗물의 총량

# 양 옆을 둘러싼 블록 중 작은 블록의 높이만큼 물이 참
# 블록의 첫 번째, 마지막에는 물이 찰 수 X
for i in range(1, col - 1):
    left_max = max(blocks[:i])
    right_max = max(blocks[i+1:])

    height_min = min(left_max, right_max)
    if blocks[i] < height_min:
        rains += (height_min - blocks[i])

print(rains)