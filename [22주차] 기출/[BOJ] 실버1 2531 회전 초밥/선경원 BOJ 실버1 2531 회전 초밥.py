
## 벨트 위에는 같은 종류의 초밥이 둘 이상 있을 수 있다.

## 쿠폰을 안 겹치게 써야 최다 종류 초밥 먹방

## 초밥 접시 수, 초밥 가짓수, 연속먹방 개수, 쿠폰 번호 입력

n, d, k, c = map(int,input().split())  



sushi = []
for _ in range(n):
  sushi.append(int(input()))

## 회전초밥은 리스트가 계속 반복되는 구조
## 슬라이싱은 한계가 있음
## 나머지를 활용해보자

## 투 포인터

left, right = 0, k
answer = 0

while left < n:
  
  s = set()

  for i in range(left, right):
    s.add(sushi[i%n])

  if c not in s:
    s.add(c)

  answer = max(answer, len(s))
  
  left += 1
  right += 1

print(answer)