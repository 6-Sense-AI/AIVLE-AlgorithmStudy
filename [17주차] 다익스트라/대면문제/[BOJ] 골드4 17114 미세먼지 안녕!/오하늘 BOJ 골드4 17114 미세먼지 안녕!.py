import sys
input = sys.stdin.readline

r,c,t = map(int, input().split()) # 세로 가로 초
arr = [list(input().strip()) for _ in range(r)]

# 상하좌우
dx = [-1,1,0,0]
dy = [0,0,-1,1]

