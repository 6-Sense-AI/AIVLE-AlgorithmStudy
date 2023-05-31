import sys 
input = sys.stdin.readline

n = int(input())
cards = list(map(int, input().split()))
m = int(input())
checks = list(map(int, input().split()))

# 이진 탐색을 위해서는 정렬 필요
cards.sort()

# 나왔던 숫자에 대해 저장할 딕셔너리
cards_dict = dict()

# 이진 탐색 함수 생성
def binary_search(array, number):    # array에서 number를 찾음
    start, end = 0, len(array) - 1
    while start <= end:
        mid = (start + end) // 2
        
        if array[mid] == number:
            tmp = cards[start:end+1].count(number)
            cards_dict[number] = tmp
            return tmp
        elif array[mid] < number:
            start = mid + 1
        else:
            end = mid - 1
    
    cards_dict[number] = 0        
    return 0
            
for c in checks:
    if c in cards_dict:
        print(cards_dict[c], end=' ')
    else:
        print(binary_search(cards, c), end=' ')