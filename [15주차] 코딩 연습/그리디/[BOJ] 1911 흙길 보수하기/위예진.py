import sys
input = sys.stdin.readline

# 입력 받기
# n: 웅덩이의 수, l: 널빤지의 크기
n, l = map(int, input().split())
# 웅덩이의 위치 정보 입력 받기
pool = [list(map(int, input().split())) for _ in range(n)]

# 웅덩이 정렬
pool.sort()

# 널빤지의 개수, 웅덩이를 덮은 널빤지의 마지막 위치 
res, now = 0, 0
for srt, end in pool:
  # 마지막 웅덩이의 위치 고려해주기
  now = max(srt, now)    

  diff = end - now    # 웅덩이의 너비
  count = (diff + l - 1) // l    # 필요한 널빤지의 수 계산
  res += count    # 널빤지 수 더해주기

  # 널빤지를 추가한만큼의 위치에서 다시 시작하도록 위치 변경해주기
  now += count * l

print(res)