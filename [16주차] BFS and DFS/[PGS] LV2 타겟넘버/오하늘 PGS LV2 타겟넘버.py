numbers = [1, 1, 1, 1, 1]
target = 3

## 사용방법 : list

def solution(numbers, target):
    answer = 0
    
    arr = [0] # 처음에 0을 넣어주지 않으면 arr값이 없어서 for문이 돌지 않음
    for i in numbers:
        tmp = []
        for j in arr:
            tmp.append(j+i) # +
            tmp.append(j-i) # -
        arr = tmp # arr에 중도 저장 이러면 arr는 마지막의 모든 경우의 수를 알게 됨
    answer = arr.count(target) # count 사용! 타겟과 같은 수의 갯수 반환해줌
    return answer