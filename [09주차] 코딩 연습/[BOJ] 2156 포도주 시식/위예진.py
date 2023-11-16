# 포도주 시식
# 가장 많은 양의 포도주를 마실 수 있도록
# 1. 포도주 잔을 선택하면 그 잔에 들어있는 포도주는 모두 마셔야 하고, 마신 후에는 원래 위치에 다시 놓아야 한다.
# 2. 연속으로 놓여 있는 3잔을 모두 마실 수는 없다.
import sys
input = sys.stdin.readline

cups = int(input())    # 포도주 잔의 수
liters = [int(input()) for _ in range(cups)]

print(liters)

