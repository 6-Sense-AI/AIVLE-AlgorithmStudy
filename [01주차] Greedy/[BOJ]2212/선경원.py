
import sys

n = int(sys.stdin.readline())
k = int(sys.stdin.readline())
sensor = sorted(list(map(int, sys.stdin.readline().split())))


if k >= n:
    print(0)
    sys.exit()  
    
## 집중국이 센서보다 많으면 센서 위치에 집중국을 설치 
##거리의 합은 0


sen_diff = []
for i in range(1, n):
    sen_diff.append(sensor[i] - sensor[i-1])

## 센서가 집중국보다 많다면, 센서가 많이 몰려 있는 곳에 집중국을 먼저 설치해야 한다.
## 한 센서와 그 다음 센서 사이 거리를 모두 구해서 다른 리스트에 담는다.


sen_diff.sort(reverse=True)
for _ in range(k-1):
    sen_diff.pop(0)
    
## 센서 간 거리가 큰 경우 서로 다른 집중국을 이용하게 해야 거리를 최소화할 수 있다.
## k개의 집중국을 사용하므로 0부터 k-1 까지 반복문을 돌리면서
## 내림차순 정렬한 센서 사이 거리 리스트에서 가장 큰 거리를 제거한다.

print(sum(sen_diff))
